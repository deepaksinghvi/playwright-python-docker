from playwright.sync_api import sync_playwright

def perform_complex_interaction():
    with sync_playwright() as p:
        print("Launching browser in headless mode...")
        browser = p.chromium.launch(headless=True)  # Headless mode
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        try:
            # Navigate to the user's GitHub page
            print("Navigating to the GitHub page...")
            page.goto("https://github.com/deepaksinghvi")

            # Click on the "Repositories" link
            print("Clicking on 'Repositories' link...")
            page.get_by_role("link", name="Repositories").click()
            
            # Find the repository search input and search for "python-one"
            print("Searching for the repository 'python-one'...")
            search_input = page.get_by_placeholder("Find a repository…")
            search_input.click()
            search_input.fill("python-one")
            search_input.press("Enter")

            # Click on the "python-one-off-dyno" repository link
            print("Clicking on 'python-one-off-dyno' repository link...")
            page.get_by_role("link", name="python-one-off-dyno").click()

            # Navigate back to the user's profile from the repository header
            print("Navigating back to the user's profile...")
            page.locator("#repository-container-header").get_by_role("link", name="deepaksinghvi").click()

            # Click on "catalogwf" label (assuming it is a button or a clickable element)
            print("Clicking on 'catalogwf' label...")
            page.get_by_label("catalogwf").click()

            # Click on the "cmd" directory link
            print("Clicking on 'cmd' directory link...")
            page.get_by_role("link", name="cmd, (Directory)").click()

            # Navigate back to the user's profile again
            print("Navigating back to the user's profile again...")
            page.get_by_role("link", name="deepaksinghvi").click()

            # Click on "cdule" label (assuming it is a button or a clickable element)
            print("Clicking on 'cdule' label...")
            page.get_by_label("cdule").click()

            # Navigate to "Issues" section
            print("Navigating to the 'Issues' section...")
            page.get_by_role("link", name="Issues Issues").click()

            # Click on the specific issue link
            print("Clicking on the specific issue link...")
            page.get_by_role("link", name="Issue with creating job_histories table due to duplicate column name.", exact=True).click()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Closing the browser...")
            context.close()
            browser.close()

if __name__ == "__main__":
    for x in range(10):
        print(x)
        perform_complex_interaction()
