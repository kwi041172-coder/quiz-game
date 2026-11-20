"""QuizGame 클래스: 게임 전체(메뉴, 퀴즈 풀기/추가/목록, 점수)를 관리한다."""

from default_quizzes import get_default_quizzes
from input_utils import read_int, read_text
from quiz import Quiz


def calculate_score(correct_count, total_count):
    """정답 수를 100점 만점 점수로 환산한다. (소수점은 버림)"""
    if total_count == 0:
        return 0
    return correct_count * 100 // total_count


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스."""

    def __init__(self):
        self.quizzes = get_default_quizzes()  # Quiz 객체 목록
        self.best_score = None  # 최고 점수 (아직 퀴즈를 풀지 않았으면 None)

    def run(self):
        """메뉴를 반복해서 보여주고 선택에 따라 기능을 실행한다."""
        try:
            while True:
                self.show_menu()
                choice = read_int("선택: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                    break
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C 또는 입력 스트림 종료가 일어나도 비정상 종료하지 않는다
            self.shutdown()

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print()
        print("=" * 40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def play_quiz(self):
        """등록된 퀴즈를 차례로 출제하고 결과를 보여준 뒤 최고 점수를 갱신한다."""
        total_count = len(self.quizzes)

        if total_count == 0:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print()
        print(f"📝 퀴즈를 시작합니다! (총 {total_count}문제)")
        print()

        correct_count = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            if self._ask_question(quiz, number):
                correct_count += 1
            print()

        score = calculate_score(correct_count, total_count)
        self._show_result(correct_count, total_count, score)

        if self.update_best_score(score):
            print("🎉 새로운 최고 점수입니다!")

    def _ask_question(self, quiz, number):
        """퀴즈 한 문제를 출제하고, 맞혔으면 True 틀렸으면 False를 반환한다."""
        print("-" * 40)
        quiz.display(number)
        print()

        user_answer = read_int("정답 입력: ", 1, 4)

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!")
            return True

        correct_text = quiz.choices[quiz.answer - 1]
        print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({correct_text})입니다.")
        return False

    def _show_result(self, correct_count, total_count, score):
        """퀴즈 결과를 출력한다."""
        print("=" * 40)
        print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")
        print("=" * 40)

    def add_quiz(self):
        """사용자에게 문제, 선택지 4개, 정답 번호를 입력받아 퀴즈를 추가한다."""
        print()
        print("📌 새로운 퀴즈를 추가합니다.")
        print()

        question = read_text("문제를 입력하세요: ")

        choices = []
        for number in range(1, 5):
            choice = read_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = read_int("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))

        print()
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        """등록된 퀴즈의 문제 목록을 출력한다."""
        total_count = len(self.quizzes)

        if total_count == 0:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"📋 등록된 퀴즈 목록 (총 {total_count}개)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def update_best_score(self, new_score):
        """새 점수를 최고 점수와 비교해 갱신한다. 새 기록이면 True를 반환한다.

        기록이 없거나 새 점수가 더 높으면 새 기록이다. 같으면 새 기록이 아니다.
        """
        if self.best_score is None or new_score > self.best_score:
            self.best_score = new_score
            return True
        return False

    def show_best_score(self):
        """최고 점수를 출력한다. 아직 퀴즈를 풀지 않았으면 안내한다."""
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요.")
            return
        print(f"🏆 최고 점수: {self.best_score}점")

    def shutdown(self):
        """입력이 중단되었을 때 안내 메시지를 출력하고 안전하게 종료한다."""
        print("\n\n⚠️ 입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
        # (저장 기능은 파일 저장 단계에서 여기에 추가한다)