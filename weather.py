import requests
from urllib.parse import quote

def get_weather(city_name):
    # 한글 도시명을 안전하게 인코딩
    encoded_city = quote(city_name)
    # wttr.in 서비스를 이용해 한국어 데이터 요청
    url = f"https://wttr.in/{encoded_city}?format=j1&lang=ko"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # 현재 날씨 데이터 추출
        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['lang_ko'][0]['value'] if 'lang_ko' in current else current['weatherDesc'][0]['value']
        humidity = current['humidity']
        feels_like = current['FeelsLikeC']

        print(f"📍 {city_name: <5} | 🌡️ {temp:>2}°C (체감 {feels_like:>2}°C) | ☁️ {desc} | 💧 습도 {humidity}%")

    except Exception:
        print(f"⚠️ {city_name}의 정보를 가져오는 데 실패했습니다.")

def main():
    # 요청하신 6개 주요 도시 리스트
    target_cities = ["서울", "부산", "인천", "대구", "광주", "제주"]
    
    print("\n" + "="*60)
    print("      🇰🇷 대한민국 주요 도시 실시간 날씨 리포트")
    print("="*60)
    
    for city in target_cities:
        get_weather(city)
        
    print("="*60)
    
    # 추가 검색 (아이패드 자소 분리 주의: 메모장에 써서 붙여넣기 추천!)
    print("\n[추가 검색] 다른 도시가 궁금하다면 이름을 입력하세요.")
    print("(입력이 없으면 프로그램이 종료됩니다.)")
    
    search_city = input("🔍 도시명 입력: ").strip()
    if search_city:
        get_weather(search_city)
        print("="*60)

if __name__ == "__main__":
    main()
