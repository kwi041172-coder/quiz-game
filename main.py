"""나만의 퀴즈 게임 - 프로그램 시작점. 실행: python main.py"""

from quiz_game import QuizGame


def main():
    """게임 객체를 만들어 실행한다."""
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()