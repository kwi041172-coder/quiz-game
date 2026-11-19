"""나만의 퀴즈 게임 - 프로그램 시작점. 실행: python main.py"""

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


def main():
    """메뉴를 반복해서 보여주고 선택에 따라 기능을 실행한다."""
    try:
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)

            if choice == 1:
                print("📝 퀴즈 풀기 기능은 준비 중입니다.")
            elif choice == 2:
                print("📌 퀴즈 추가 기능은 준비 중입니다.")
            elif choice == 3:
                print("📋 퀴즈 목록 기능은 준비 중입니다.")
            elif choice == 4:
                print("🏆 점수 확인 기능은 준비 중입니다.")
            elif choice == 5:
                print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                break  # while 반복을 끝낸다
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 또는 입력 스트림 종료가 일어나도 비정상 종료하지 않는다
        print("\n\n⚠️ 입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
        # (저장 기능은 파일 저장 단계에서 여기에 추가한다)


if __name__ == "__main__":
    main()