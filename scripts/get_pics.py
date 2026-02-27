import requests
import os
import time
import sys

# --- 設定設定集 ---
# 這裡儲存每一天的報紙參數：(URL範本, 總張數)
ARCHIVE_CONFIG = {
    "April15": (
        "https://news.google.com/newspapers?id=YTwbAAAAIBAJ&sjid=Ak0EAAAAIBAJ&pg=864%2C5343624&img=1&hl=en&zoom=6&tid={}",
        234
    ),
    "April16": (
        "https://news.google.com/newspapers?id=YjwbAAAAIBAJ&sjid=Ak0EAAAAIBAJ&pg=928%2C5625158&img=1&hl=en&zoom=6&tid={}",
        234
    ),
    "April17": (
        "https://news.google.com/newspapers?id=YzwbAAAAIBAJ&sjid=Ak0EAAAAIBAJ&pg=928%2C5952036&img=1&hl=en&zoom=6&tid={}",
        234
    ),
    "April18": (
        "https://news.google.com/newspapers?id=ZDwbAAAAIBAJ&sjid=Ak0EAAAAIBAJ&pg=928%2C6287180&img=1&hl=en&zoom=6&tid={}",
        234
    )
}

def download_newspaper(date_key):
    if date_key not in ARCHIVE_CONFIG:
        print(f"Error: Date '{date_key}' not found in config.")
        print(f"Available dates: {list(ARCHIVE_CONFIG.keys())}")
        return

    base_url, total_pics = ARCHIVE_CONFIG[date_key]

    # 建立目錄路徑 (配合先前的結構建議放到 raw_data 下)
    output_dir = os.path.join("raw_data", date_key)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Starting download for {date_key} into {output_dir}...")

    for tid in range(0, total_pics):
        url = base_url.format(tid)
        img_path = os.path.join(output_dir, f"tile_{tid:03d}.jpg")

        # 如果檔案已存在則跳過，方便中斷後續傳
        if os.path.exists(img_path):
            continue

        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
            if response.status_code == 200:
                with open(img_path, "wb") as f:
                    f.write(response.content)
                print(f"[{date_key}] Downloaded: {tid}/{total_pics - 1}")
            else:
                print(f"[{date_key}] Failed {tid}: Status {response.status_code}")
        except Exception as e:
            print(f"[{date_key}] Error {tid}: {e}")

        time.sleep(0.1)

if __name__ == "__main__":
    # 允許從命令行輸入日期，例如: python get_pics.py April15
    if len(sys.argv) > 1:
        target_date = sys.argv[1]
        download_newspaper(target_date)
    else:
        # 如果沒輸入參數，預設跑全部（或你可以改成只跑某一天）
        for key in ARCHIVE_CONFIG.keys():
            download_newspaper(key)
