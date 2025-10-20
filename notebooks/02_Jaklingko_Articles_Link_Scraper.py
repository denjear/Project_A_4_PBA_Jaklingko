import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_driver():
    options = Options()
    # kalau mau lihat prosesnya bisa hapus headless
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)  # waktu cukup longgar biar gak timeout
    return driver

def resolve_url(url):
    driver = get_driver()
    start_time = time.time()
    result = {"Link_Asli": url, "Resolved_URL": None, "Waktu(s)": None}

    try:
        driver.get(url)
        # Tunggu redirect selesai (bukan di domain Google News)
        WebDriverWait(driver, 20).until(lambda d: "news.google.com" not in d.current_url)
        final_url = driver.current_url
        result["Resolved_URL"] = final_url
    except Exception as e:
        result["Resolved_URL"] = f"Error: {e}"
    finally:
        result["Waktu(s)"] = round(time.time() - start_time, 2)
        driver.quit()
    return result

# --- Load data ---
df = pd.read_csv("jaklingko_url.csv")
urls = df["Link"].dropna().tolist()

# --- Parallel Execution ---
max_workers = 5  # 5 browser paralel
results = []

start_all = time.time()
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(resolve_url, url): url for url in urls}
    for future in as_completed(futures):
        res = future.result()
        print(f"✅ {res['Link_Asli']} -> {res['Resolved_URL']} ({res['Waktu(s)']}s)")
        results.append(res)

elapsed_all = round(time.time() - start_all, 2)
print(f"\n🔥 Semua selesai dalam {elapsed_all} detik dengan {max_workers} browser paralel.")

# --- Simpan hasil ---
out_df = pd.DataFrame(results)
out_df.to_csv("jaklingko_resolved_parallel_stable.csv", index=False, encoding="utf-8-sig")

print("✅ Hasil disimpan ke jaklingko_resolved_parallel_stable.csv")
