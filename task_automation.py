"""
SMART TASK AUTOMATION SYSTEM – EXCELLENT & VERIFIED VERSION
Author: anishka Sharma

Features:
1. Move JPG files safely
2. Extract unique email IDs from text file
3. Scrape website title
4. Log all activities

Status: ✔ Fully correct | ✔ Error-handled | ✔ Project-ready
"""

import shutil
import re
import requests
from datetime import datetime
from pathlib import Path

LOG_FILE = "logs.txt"

# ---------------------- LOGGER ----------------------
def log_activity(message: str):
    """Logs activity with timestamp"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - {message}\n")


# ---------------------- TASK 1: MOVE JPG FILES ----------------------
def move_jpg_files(source_folder: str, destination_folder: str):
    """Moves all JPG files from source to destination"""
    try:
        src = Path(source_folder)
        dest = Path(destination_folder)

        if not src.exists() or not src.is_dir():
            raise FileNotFoundError("Source folder does not exist or is invalid")

        dest.mkdir(parents=True, exist_ok=True)

        jpg_files = [f for f in src.iterdir() if f.suffix.lower() == ".jpg"]

        for file in jpg_files:
            shutil.move(str(file), dest / file.name)

        print(f"\n✅ {len(jpg_files)} JPG file(s) moved successfully")
        log_activity(f"Moved {len(jpg_files)} JPG files")

    except Exception as e:
        print(f"❌ Error: {e}")
        log_activity(f"Error moving JPG files: {e}")


# ---------------------- TASK 2: EXTRACT EMAILS ----------------------
def extract_emails(input_file: str, output_file: str):
    """Extracts unique emails from a text file"""
    try:
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError("Input file not found")

        content = input_path.read_text(encoding="utf-8")
        emails = set(re.findall(r"[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}", content))

        Path(output_file).write_text("\n".join(sorted(emails)), encoding="utf-8")

        print(f"\n✅ {len(emails)} unique email(s) extracted")
        log_activity(f"Extracted {len(emails)} emails")

    except Exception as e:
        print(f"❌ Error: {e}")
        log_activity(f"Email extraction error: {e}")


# ---------------------- TASK 3: SCRAPE WEBSITE TITLE ----------------------
def scrape_website_title(url: str):
    """Scrapes and saves the title of a website"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        if not match:
            raise ValueError("Title tag not found")

        title = match.group(1).strip()
        Path("website_title.txt").write_text(f"Website Title: {title}", encoding="utf-8")

        print("\n✅ Website title scraped successfully")
        print(f"📌 Title: {title}")
        log_activity(f"Scraped website title: {title}")

    except Exception as e:
        print(f"❌ Error: {e}")
        log_activity(f"Web scraping error: {e}")


# ---------------------- MAIN MENU ----------------------
def main():
    while True:
        print("\n" + "=" * 55)
        print(" SMART TASK AUTOMATION SYSTEM ")
        print("=" * 55)
        print("1. Move all JPG files")
        print("2. Extract Email Addresses")
        print("3. Scrape Website Title")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            move_jpg_files(
                input("Enter source folder path: ").strip(),
                input("Enter destination folder path: ").strip(),
            )

        elif choice == "2":
            extract_emails("emails_input.txt", "extracted_emails.txt")

        elif choice == "3":
            scrape_website_title(input("Enter website URL (https://...): ").strip())

        elif choice == "4":
            print("\n👋 Exiting program. Thank you!")
            log_activity("Program exited by user")
            break

        else:
            print("❌ Invalid choice. Please select 1–4")


# ---------------------- PROGRAM START ----------------------
if __name__ == "__main__":
    main()
