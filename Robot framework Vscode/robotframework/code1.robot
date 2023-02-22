*** Settings ***
Library    SeleniumLibrary
Resource    ../robotframework/Operations/code1ops.robot
#Library    RPA.Browser.selenium     auto close=${False}
*** Variables ***

${url1}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome
*** Test Cases ***
login_Test
    Open Browser    ${url1}    ${browser}
    Maximize Browser Window
    Login_to_orangehrm
    
    


   