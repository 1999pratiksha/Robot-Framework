*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
Login_to_orangehrm
    Sleep    7
#    Title Should Be    OrangeHRM
    ${Title}    Get Title

    ${userbox}    Set Variable     xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]    
    Element Should Be Enabled    ${userbox}
    Element Should Be Visible    ${userbox}
    Input Text     ${userbox}    Admin
    Sleep    5
    Press Key    ${userbox}   CTRL+A+DELETE
    Sleep    5
#   Input Text    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]    Admin
#   Sleep    6
#   Input Text    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]    admin123
#   Click Element    xpath://body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]
#   Sleep    6
#   Click Element    xpath://header/div[1]/div[2]/ul[1]/li[1]/span[1]/i[1]
#   Click Element    xpath://a[contains(text(),'Logout')]
#   Sleep    3