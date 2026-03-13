import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # 1. 기회 제한 설정 (게임의 긴장감!)
    
    print("=== 🎯 UP & DOWN 숫자 맞추기 게임 ===")
    print(f"1부터 100 사이의 숫자를 맞춰보세요. 기회는 {max_attempts}번입니다.")

    while attempts < max_attempts:
        try:
            # 남은 기회 표시
            print(f"\n[남은 기회: {max_attempts - attempts}번]")
            guess = int(input("숫자 입력: "))

            # 2. 범위 유효성 검사
            if guess < 1 or guess > 100:
                print("❌ 에러: 1에서 100 사이의 숫자만 입력해주세요!")
                continue

            attempts += 1

            # 3. UP & DOWN 핵심 로직
            if guess < secret_number:
                print("▲ UP! 더 큰 숫자를 불러보세요.")
            elif guess > secret_number:
                print("▼ DOWN! 더 작은 숫자입니다.")
            else:
                print(f"🎊 정답입니다! {attempts}번 만에 맞추셨네요!")
                return # 게임 종료

        except ValueError:
            print("⚠️ 숫자가 아닌 문자는 입력할 수 없어요.")

    # 기회를 모두 소진했을 때
    print(f"\n💀 게임 오버! 정답은 {secret_number}였습니다. 다시 도전해보세요!")

# 게임 실행
start_game()