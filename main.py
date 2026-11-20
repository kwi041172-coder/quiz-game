"""나만의 퀴즈 게임 - 프로그램 시작점. 실행: python main.py"""

from default_quizzes import get_default_quizzes
from input_utils import read_int


def show_menu():
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


def calculate_score(correct_count, total_count):
    """정답 수를 100점 만점 점수로 환산한다. (소수점은 버림)"""
    if total_count == 0:
        return 0
    return correct_count * 100 // total_count


def ask_question(quiz, number):
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


def show_result(correct_count, total_count):
    """퀴즈 결과를 출력한다."""
    score = calculate_score(correct_count, total_count)
    print("=" * 40)
    print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)


def play_quiz(quizzes):
    """퀴즈 목록을 차례로 출제한다.

    퀴즈가 없으면 안내 후 None을 반환한다.
    끝까지 풀었으면 (정답 수, 전체 문제 수)를 반환한다.
    """
    total_count = len(quizzes)

    if total_count == 0:
        print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return None

    print()
    print(f"📝 퀴즈를 시작합니다! (총 {total_count}문제)")
    print()

    correct_count = 0
    for number, quiz in enumerate(quizzes, start=1):
        if ask_question(quiz, number):
            correct_count += 1
        print()

    show_result(correct_count, total_count)
    return correct_count, total_count


def main():
    """메뉴를 반복해서 보여주고 선택에 따라 기능을 실행한다."""
    quizzes = get_default_quizzes()

    try:
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)

            if choice == 1:
                play_quiz(quizzes)
            elif choice == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("🏆 점수 확인 기능은 준비 중입니다.")
            elif choice == 5:
                print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                break
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 또는 입력 스트림 종료가 일어나도 비정상 종료하지 않는다
        print("\n\n⚠️ 입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
        # (저장 기능은 파일 저장 단계에서 여기에 추가한다)


if __name__ == "__main__":
    main()