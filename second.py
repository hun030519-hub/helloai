import random

def start_word_game():
    # 1. 맞출 단어 후보들 (리스트 문법)
    words = ["python", "github", "coding", "deploy", "variable", "function"]
    target_word = random.choice(words) # 랜덤으로 하나 선택
    
    guessed_letters = [] # 사용자가 입력한 글자들을 저장할 리스트
    attempts = 6 # 남은 목숨

    print("=== 🔠 파이썬 단어 맞추기 챌린지 ===")
    print("컴퓨터가 생각한 단어를 한 글자씩 맞춰보세요!")

    while attempts > 0:
        # 2. 현재 맞춘 상태 보여주기 (List Comprehension & Join 문법)
        # 단어의 각 글자를 확인해서 맞춘 글자는 보여주고, 아니면 '_' 표시
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in target_word])
        print(f"\n현재 단어: {display_word}")
        print(f"남은 목숨: {'❤️' * attempts}")
        print(f"입력했던 글자들: {', '.join(guessed_letters)}")

        # 모든 글자를 다 맞췄다면 종료
        if "_" not in display_word:
            print(f"🎊 대단해요! 정답은 '{target_word}'였습니다!")
            break

        # 3. 사용자 입력 받기
        guess = input("알파벳 한 글자를 입력하세요: ").lower()

        # 유효성 검사 (한 글자인지, 알파벳인지)
        if len(guess) != 1 or not guess.isalpha():
            print("❌ 알파벳 한 글자만 입력해 주세요.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ '{guess}'는 이미 입력한 글자입니다.")
            continue

        guessed_letters.append(guess)

        # 4. 정답 확인 로직
        if guess in target_word:
            print(f"✅ 오! '{guess}'가 포함되어 있네요!")
        else:
            attempts -= 1
            print(f"❌ 아쉽습니다. '{guess}'는 단어에 없습니다.")

    if attempts == 0:
        print(f"\n💀 게임 오버! 정답은 '{target_word}'였습니다. 다음에 다시 도전하세요!")

start_word_game()
