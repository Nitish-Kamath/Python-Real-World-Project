import webbrowser as wb

def webauto():
    chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe  %s'   #adding the path of chrome
    URLS={
        "stackoverflow.com",
        "github.com",
        "gmail.com",
        "google.com",
        "youtube.com"
    }
    for url in URLS:
        print("opening:" + url)
        wb.get(chrome_path).open(url)
webauto()