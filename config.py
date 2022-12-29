from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10248430
    API_HASH = "42396a6ff14a569b9d59931643897d0d"
    # the name to display in your alive message
    ALIVE_NAME = "rishabh"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://yjjdrfpn:a5IfsOT5ZxivwDDOXjLDUQQJp6OzRfPN@satao.db.elephantsql.com/yjjdrfpn"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzkBu2UCDrocccmeR0dGY4EEbSiwdjXyhyFCzZYuLVOPFFGwTf1HfHC8SdNvce-WpIqroOiPwSfXlui_Pu8n9ndh6u8ez94XX2_raKCcAusYPZy6fR0h63eFS1ENrTV0Dt9ZmFTU_A0B90sciBHnhN4npt0z2KFT5GtolwYc8oq2xcZEwnVu_MLqap1UAi_32Bc5FhDHV7cCIVf3htSy-cH4NxDI1m1LmpimhtQdJUaBetYtQtmPX9Hzyk6wxxqHbUDM-ZXGwrhbT58PyH1ATZdYDdpQLeiCchrMtt8tJgyg-1XUCtA3alMo-v2SpdeqIklqPk5lhiKNAL2Ykb_rt_xW8po="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5842499336:AAHORYhD6U8QBHgi2V5m2w23NFuvS6ISJsY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001638711701
    # command handler
    COMMAND_HAND_LER = "."
    VCMODE = "False"
    #VC_SESSION = "your 2nd id telethon session" #note don't use maim account to vc player
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/rishabhanand2/tha_plugins"
    #don't edit this 
    THANOSABUSE = "False"#don't edit this else error in 
