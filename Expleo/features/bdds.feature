Feature: XE Testing


  Scenario: Logo is visible
     Given: the logo is visible
     When: the user opens the page
     Then: logo should be visible  

  Scenario: Successfully converting 50 dollars to pounds
    Given the user can open Xe Currency Converter website
    Then on Amount field the user should input 50 value
    Then on From options the user should click on the field
    And dropdown menu should open to search by typing or selecting the USD - US Dollar
    Then on To field the user should click on the field
    And dropdown menu should open to search by typing or selecting the GBP - British Pound
    Then clicking on Convert button the expect result about the conversion should appears  ****42.71

  Scenario: Successfully converting 50 Brazilian  Real to Japanese Yen
    Given the user can open Xe Currency Converter website
    Then on Amount field the user should input 50 value
    Then on From options the user should click on the field
    And dropdown menu should open to search by typing or selecting the BRL - Brazilian Real
    Then on To field the user should click on the field
    And dropdown menu should open to search by typing or selecting the JPY - Japanese Yen
    Then clicking on Convert button the expect result about the conversion should appears

  Scenario: Inserting words instead of numbers in the Amount field
    Given the user can open Xe Currency Converter website
    Then on Amount field the user should input text (Testing text as example)
    And a error message containing the text “ Please enter a valid amount” should appears

  Scenario: Performing a Pounds to Argentine Pesos conversion with wrong result
    Given the user can open Xe Currency Converter website
    Then on Amount field the user should input 50 value
    Then on From options the user should click on the field
    And dropdown menu should open to search by typing or selecting the GBP - Britsh Pound
    Then on To field the user should click on the field
    And dropdown menu should open to search by typing or selecting the ARS - Argentine Peso
    Given the user inputs the correct value and exchange data for the conversion
    Then clicking on Convert button the not expect result i'll show
  

  Scenario: Performing the conversion from BRL to YEN and then reversing the conversion using the "Swap currencies" button
    Given the user can open Xe Currency Converter website
    Then on Amount field the user should input 50 value
    Then on From options the user should click on the field
    And dropdown menu should open to search by typing or selecting the BRL - Brazilian Real
    Then on To field the user should click on the field
    And dropdown menu should open to search by typing or selecting the JPY - Japanese Yen
    Then clicking on Convert button the expect result about the conversion should appears
    And clicking on “Swap currencies” button the currencies must be exchanged with each other now presenting inverse values from YEN to BRL
