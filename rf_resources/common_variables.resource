*** Settings ***
Documentation     Variables communes — Epignosis CRM Demo
...               Remplace automationplayground.com/crm

*** Variables ***
${BROWSER}              chrome
${START_URL}            http://localhost:5000

# Identifiants de test
${VALID_EMAIL}          admin@fakeemail.com
${VALID_PASSWORD}       SecretSauce!25

# Textes de vérification
${HOME_TEXT}            Les Clients Sont Notre Priorité
${LOGIN_SUCCESS_TEXT}   Nos Clients Satisfaits
${ADD_CUSTOMER_TEXT}    Ajouter un Client
${SUCCESS_TEXT}         Succès – Nouveau Client Ajouté
${ERROR_LOGIN_TEXT}     Invalid Login Credentials

# Locateurs — Page de connexion (identiques à automationplayground)
${LOGIN_LINK}               Sign In
${LOGIN_EMAIL_FIELD}        id=email-id
${LOGIN_PASSWORD_FIELD}     id=password
${LOGIN_REMEMBER_CHECKBOX}  id=remember
${LOGIN_SUBMIT_BUTTON}      id=submit-id

# Locateurs — Page clients
${ADD_CUSTOMER_LINK}        id=new-customer

# Locateurs — Formulaire nouveau client (identiques à automationplayground)
${EMAIL_FIELD}          id=EmailAddress
${FIRSTNAME_FIELD}      id=FirstName
${LASTNAME_FIELD}       id=LastName
${CITY_FIELD}           id=City
${STATE_FIELD}          id=StateOrRegion
${PROMOS_CHECKBOX}      name=promos-name
${SUBMIT_BUTTON}        id=submit-id
${SUCCESS_MESSAGE}      id=Success

# Données de test françaises
${TEST_EMAIL_1}         laura.martin@test.fr
${TEST_PRENOM_1}        Laura
${TEST_NOM_1}           Martin
${TEST_VILLE_1}         Paris
${TEST_REGION_1}        IDF
${TEST_GENRE_1}         female

${TEST_EMAIL_2}         jean.dupont@test.fr
${TEST_PRENOM_2}        Jean
${TEST_NOM_2}           Dupont
${TEST_VILLE_2}         Lyon
${TEST_REGION_2}        ARA
${TEST_GENRE_2}         male

${TEST_EMAIL_3}         emma.petit@test.fr
${TEST_PRENOM_3}        Emma
${TEST_NOM_3}           Petit
${TEST_VILLE_3}         Marseille
${TEST_REGION_3}        PAC
${TEST_GENRE_3}         female
