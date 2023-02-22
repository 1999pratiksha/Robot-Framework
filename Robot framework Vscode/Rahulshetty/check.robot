** Settings ***
Library    SeleniumLibrary
Library    XML
#Library    RPA.Browser.selenium     auto close=${False}
*** Variables ***

${url}    https://rahulshettyacademy.com/dropdownsPractise/   
${browser}    chrome
*** Keywords ***
Flights_check
    Sleep    7
    Click Element    xpath://input[@id='ctl00_mainContent_rbtnl_Trip_1'] 
    Sleep    2
    # Select From List By Label    ctl00_mainContent_DropDownListCurrency    AED  
    Select From List By Index   //select[@id='ctl00_mainContent_DropDownListCurrency']    2
    Select Checkbox    xpath://input[@id='ctl00_mainContent_chk_friendsandfamily']
    Sleep    4
    Close Browser    

*** Test Cases ***
login_Test
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Flights_check