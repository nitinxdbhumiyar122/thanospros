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
    STRING_SESSION = "1BVtsOKwBu4PgWEo02X6yjWI8yN8rjZMfBhKaFnv8luzSB2ndnOS2p9xaAmAdVsm4FkaA2qPoaXvW8yrnzIcykn98K8xjpsF7Z8MfAv5NlzY1rawUmXRKoeeziTSf_pCP0Dx-M4VIUf8tsFW9iQ3oEy62DQ66TqSKm6j_SyXokah1mLqx9rMOa7nZ4xGWJsDd9ZUaEILjfy6HlfLhkUqzL5NJWqROVYx9ysee63kXI54ELgr_usdyZNP5RWIcZb_6BT8HxdXlxyOfcwydBEYuCc3S4anRPD4-biHx7GqoVxLlDiQrQ_3Yp4RcmnjJUz4qFUPcM9aAQ7owOuEJVLF_2HyXksEqrwg="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6188490070:AAHG9pHbiNRrSc9Uu0sHD26Dx8m4s67NSg4"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001835490248
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
