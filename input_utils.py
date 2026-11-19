"""공통 입력 함수 모음.

사용자 입력을 받을 때 생기는 대표적인 문제(빈 입력, 숫자가 아닌 입력,
범위 밖 숫자)를 한 곳에서 처리한다.

주의: KeyboardInterrupt(Ctrl+C)와 EOFError(입력 스트림 종료)는
여기서 처리하지 않고 호출한 쪽(프로그램 최상위)으로 그대로 전달한다.
"""


def read_text(prompt):
    """빈 값이 아닌 문자열을 입력받아 반환한다."""
    while True:
        text = input(prompt).strip()  # 앞뒤 공백 제거
        if text == "":
            print("⚠️ 빈 입력입니다. 내용을 입력해 주세요.")
            continue  # 처음(while)으로 돌아가 다시 입력받는다
        return text


def read_int(prompt, min_value, max_value):
    """min_value ~ max_value 사이의 정수를 입력받아 반환한다."""
    while True:
        text = input(prompt).strip()  # 앞뒤 공백 제거

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
            continue

        try:
            number = int(text)  # 문자열을 정수로 변환 시도
        except ValueError:
            print(f"⚠️ 숫자가 아닙니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if number < min_value or number > max_value:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number  # 모든 검사를 통과한 올바른 값