import random

def play_game():
    # 맞출 단어 후보 리스트
    words = ['python', 'github', 'programming', 'developer', 'algorithm', 'interface']
    target_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6  # 허용되는 틀린 횟수

    print("=== 파이썬 단어 맞추기 게임 ===")
    print(f"힌트: {len(target_word)}글자의 단어입니다.")

    while attempts > 0:
        # 현재까지 맞춘 상태 표시
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        
        print(f"\n현재 단어: {display_word}")
        print(f"남은 기회: {attempts}")
        
        if "_ " not in display_word:
            print(f"축하합니다! 단어를 맞췄습니다: {target_word}")
            break

        guess = input("알파벳 한 글자를 입력하세요: ").lower()

        # 입력 유효성 검사
        if len(guess) != 1 or not guess.isalpha():
            print("올바른 알파벳 한 글자만 입력해주세요.")
            continue

        if guess in guessed_letters:
            print(f"이미 입력했던 글자입니다: '{guess}'")
            continue

        guessed_letters.append(guess)

        if guess in target_word:
            print(f"정답! '{guess}'가 포함되어 있습니다.")
        else:
            attempts -= 1
            print(f"땡! '{guess}'는 없습니다.")

    if attempts == 0:
        print(f"\n아쉽네요! 기회를 모두 소진했습니다. 정답은 '{target_word}'였습니다.")

if __name__ == "__main__":
    play_game()
