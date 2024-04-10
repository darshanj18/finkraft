import requests
from bs4 import BeautifulSoup


def perform_google_search(query: str) -> str:
    base_url = 'https://www.google.com/search'
    params = {'q': query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Will help to know if the request was blocked
        return response.text
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return ""


def parse_search_results(html_content: str):
    soup = BeautifulSoup(html_content, 'html.parser')
    results = []
    for result in soup.select('.tF2Cxc'):  # Ensuring class .tF2Cxc is still valid
        title = result.select_one('h3').text if result.select_one('h3') else 'No Title'
        link = result.select_one('a')['href'] if result.select_one('a') else 'No Link'
        results.append({
            'title': title,
            'link': link
        })
        if len(results) == 10:
            break
    return results


def main():
    query = input("Enter your search query: ")
    html_content = perform_google_search(query)

    if html_content:
        results = parse_search_results(html_content)
        if results:
            for result in results:
                print(result)
        else:
            print("No results found.")
    else:
        print("Failed to retrieve search results.")


if __name__ == "__main__":
    main()
