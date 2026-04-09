def calculator():
    print("="*30)
    print("   파이썬 심플 계산기")
    print("="*30)
    print("사용 가능 연산: +, -, *, /")
    print("종료하려면 '종료'를 입력하세요.")

    while True:
        user_input = input("\n계산식 입력 (예: 10 + 20): ").strip()

        if user_input == "종료":
            print("계산기를 종료합니다.")
            break

        try:
            # 입력받은 문자열을 공백 기준으로 분리
            parts = user_input.split()
            
            if len(parts) != 3:
                print("입력 형식이 잘못되었습니다. (예: 10 + 5)")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("오류: 0으로 나눌 수 없습니다.")
                    continue
                result = num1 / num2
            else:
                print("지원하지 않는 연산자입니다.")
                continue

            print(f"결과: {result}")

        except ValueError:
            print("오류: 숫자 형식이 올바르지 않습니다.")

if __name__ == "__main__":
    calculator()