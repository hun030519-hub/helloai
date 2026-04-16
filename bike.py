import pandas as pd

def search_bike_station():
    # 1. 업로드하신 파일 읽기
    file_name = 'busan_bike.csv'
    try:
        df = pd.read_csv(file_name, encoding='utf-8-sig')
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_name}")
        return

    print("=== 🚲 부산 자전거 대여소 검색기 (강서/북구/사상구) ===")
    print("현재 검색 가능한 구: 강서구, 북구, 사상구")
    
    user_gu = input("\n검색하고 싶은 '구' 이름을 입력하세요 (예: 사상구): ").strip()

    # 2. 도로명주소 또는 지번주소에서 검색 (문자열 변환 후 검색)
    mask = (df['소재지도로명주소'].astype(str).str.contains(user_gu, na=False) | 
            df['소재지지번주소'].astype(str).str.contains(user_gu, na=False))
    
    result = df[mask]

    # 3. 결과 출력
    if result.empty:
        print(f"\n❌ '{user_gu}'에 대한 검색 결과가 없습니다.")
        print("팁: 업로드된 파일에는 '강서구', '북구', '사상구' 데이터만 들어있습니다.")
    else:
        print(f"\n✅ [{user_gu}] 지역 대여소 검색 결과입니다:")
        print("-" * 60)
        for _, row in result.iterrows():
            # 주소가 있는 항목 선택
            addr = row['소재지도로명주소'] if pd.notna(row['소재지도로명주소']) else row['소재지지번주소']
            
            print(f"📍 명칭: {row['자전거대여소명']}")
            print(f"   위치: {addr}")
            print(f"   보유: {row['자전거보유대수']}대 (운영: {row['운영시작시각']}~{row['운영종료시각']})")
            print("-" * 60)

if __name__ == "__main__":
    search_bike_station()
    