"""Quiz 클래스: 퀴즈 한 문제를 표현한다."""


class Quiz:
    """퀴즈 한 문제 (문제, 선택지 4개, 정답 번호 1~4)."""

    def __init__(self, question, choices, answer):
        # 잘못된 데이터로 퀴즈가 만들어지는 것을 막는다
        if not isinstance(question, str) or question.strip() == "":
            raise ValueError("문제는 비어 있지 않은 문자열이어야 합니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개의 항목을 가진 리스트여야 합니다.")
        if not isinstance(answer, int) or not 1 <= answer <= 4:
            raise ValueError("정답은 1~4 사이의 정수여야 합니다.")

        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number=None):
        """문제와 선택지를 화면에 출력한다. number가 있으면 [문제 N]을 붙인다."""
        if number is not None:
            print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False를 반환한다."""
        return user_answer == self.answer

    def to_dict(self):
        """파일(JSON) 저장용으로 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """저장된 딕셔너리에서 Quiz 객체를 복원한다."""
        try:
            return cls(data["question"], data["choices"], data["answer"])
        except (KeyError, TypeError):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")