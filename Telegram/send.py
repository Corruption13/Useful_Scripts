import telegram
token=''
def send_mail(chat_id,message):
    send=telegram,Bot(token=token)
    try:
        send.sendMessage(chat_id,text=msg)
        print("sent succesfully")
    except:
        print("Error!!!")

if __name__='__main__':
    config_file=sys.arv[1]
    message_file=sys.argv[2]a
    with open(config_file) as file:
        configs=file.split(',')
    token=configs[0]
    chat_id=configs[1]
    with open(message_file) as file:
        message=file
    send_mail(token,chat_id,message)
