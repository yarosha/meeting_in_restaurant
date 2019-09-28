def help():
    print(1)

def students(people, people_want, days):
    finaly_version = [[]]
    tables = 13
    keys = []
    vals = []
    keys2 = []
    vals2 = []
    tuesday = []
    monday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    datas = {}
    indexer = []
    counter = 0
    string1 = []
    string2 = []
    final_version = []
    maxs = 0
    maxss = []
    final_version1 = []
    print("students")
    for keyses, values in people.items():
        keys.append(keyses)
        vals.append(values)
        print("add to some shit")

    for keyses2, values2 in days.items():
        keys2.append(keyses2)
        vals2.append(values2)
        print("add to some shit2")
    print("keys")
    print(keys)
    print(keys2)
    print("vals")
    print(vals)
    print(vals2)
    for i in range(0, len(vals)):
        vals[i] = vals[i].split(',')

    for i in range(0, len(vals2)):  ###заполняем людей, которые хотят пойти в понедельник
        if vals2[i] == 1:
            monday.append(keys2[i])
            print("add to monday")

        elif vals2[i] == '2':  ###заполняем людей, которые хотят пойти во вторник
            tuesday.append(keys2[i])

        elif vals2[i] == '3':  ###заполняем людей, которые хотят пойти в среду
            wednesday.append(keys2[i])

        elif vals2[i] == '4':  ###заполняем людей, которые хотят пойти в четверг
            thursday.append(keys2[i])

        elif vals2[i] == '5':  ###заполняем людей, которые хотят пойти в пятницу
            friday.append(keys2[i])

        elif vals2[i] == '6':  ###заполняем людей, которые хотят пойти в субботу
            saturday.append(keys2[i])
    for i in range(0, len(monday)):
        indexer.append(monday[i])
    df = pd.DataFrame(data=None, index=indexer, columns=indexer)

    for i in range(0, len(monday)):
        for j in range(0, len(monday)):
            counter = 0
            string1 = people[monday[i]].split(',')
            string2 = people[monday[j]].split(',')
            if i != j:
                for a in range(0, len(string1)):
                    if ((string1[a] == string2[a]) and (string1[a] == '1')):
                        counter += 1
                        df.loc[monday[i], monday[j]] = counter
                    elif (string1[a] != string2[a]):
                        pass
    for i in range(0, len(monday)):
        for j in range(0, len(monday)):
            if df.loc[monday[i], monday[j]] == None:
                df.loc[monday[i], monday[j]] = 0
    print("MOnday")
    print(len(monday))
    # while (a != 0) or (a != 1):
    print(df)
    for i in range(0, len(monday) - 2):
        print("loop before df")
        for j in range(0, len(monday) - 2):
            if i != j:
                print("maxs df.loc")
                print(maxs)
                print(df.loc[monday[i], monday[j]])
                if maxs < df.loc[monday[i], monday[j]]:
                    print("Here is trouble")
                    maxs = df.loc[monday[i], monday[j]]
                    maxss = [monday[i], monday[j]]
        if len(monday) >= 3:
            print('b')
            print("maxss")
            print(maxss)
            print(len(maxss))
            final_version.append([maxss[0], maxss[1]])
            print(final_version)
            monday.remove(maxss[0])
            monday.remove(maxss[1])
            del df[maxss[0]]
            del df[maxss[1]]
            df = df.drop(maxss[0], axis='index')
            df = df.drop(maxss[1], axis='index')
            maxs = 0
        print("debug0")
        print(df)
    print(monday)
    return final_version


def functional_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Хочу свиданку', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Хочу фильм', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Хочу книгу', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    keyboard.add_button('Что тут вообще происходит?', color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard


def Help(people, people_today, days_of_week):
  print(1)
  array = students(people, people_today, days_of_week)
  print("debug1")
  print(array)
  for i in range(len(array)):
    vk.method("messages.send",{"peer_id" : str(students(people, people_today, days_of_week)[i][0]), "message" : 'Сегодня за обедом приходи и садись за 3 столик', "random_id": (r.uniform(0, 2**32))})
    vk.method("messages.send", {"peer_id": str(students(people, people_today, days_of_week)[i][1]),"message": 'Сегодня за обедом приходи и садись за 3 столик', "random_id": (r.uniform(0, 2 ** 32))})

def days_keyboard():
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Понедельник', color=VkKeyboardColor.POSITIVE)

    #keyboard.add_button('Вторник', color=VkKeyboardColor.POSITIVE)
    #keyboard.add_line()

    #keyboard.add_button('Среда', color=VkKeyboardColor.PRIMARY)
    #keyboard.add_button('Четверг', color=VkKeyboardColor.PRIMARY)
    #keyboard.add_line()

    #keyboard.add_button('Пятница', color=VkKeyboardColor.NEGATIVE)
    #keyboard.add_button('Суббота', color=VkKeyboardColor.NEGATIVE)

    keyboard = keyboard.get_keyboard()
    return keyboard


def create_keyboard():
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Да', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Нет', color=VkKeyboardColor.PRIMARY)
    keyboard = keyboard.get_keyboard()

    return keyboard

def functional_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Хочу свиданку', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Хочу фильм', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Хочу книгу', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    keyboard.add_button('Что тут вообще происходит?', color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard




import vk_api, time, schedule, datetime
import pandas as pd
import random as r
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

people_today = []
people = {}
status = {}
days_of_week = {}
basa = {}
pp=0

tables_photo = ['photo-183224626_456239028', 'photo-183224626_456239027', 'photo-183224626_456239026',
                'photo-183224626_456239025', 'photo-183224626_456239024', 'photo-183224626_456239024',
                'photo-183224626_456239024', 'photo-183224626_456239023', 'photo-183224626_456239022',
                'photo-183224626_456239021', 'photo-183224626_456239020', 'photo-183224626_456239019',
                'photo-183224626_456239018', 'photo-183224626_456239038']
films_photo = ['photo-183224626_456239033', 'photo-183224626_456239034', 'photo-183224626_456239035',
               'photo-183224626_456239036', 'photo-183224626_456239037']
vk = vk_api.VkApi(token='7130525f3afeea47df11b62cf7cc4c4c1aae6663106fafa6acd72b7643660c9e847f69442c4e0e19e659f')
vk._auth_token()

#schedule.every().day.at("03:15").do(Help,[people, people_today, days_of_week])
a=1
while True:
    if (a==1) and (pp==4):
      print(pp)
      a=2
      Help(people, people_today, days_of_week)
      #do_something(people, people_today, days_of_week)
    else:
      messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
      if messages["count"] >= 1:
          user_id = messages["items"][0]["last_message"]["from_id"]
          text = messages["items"][0]["last_message"]["text"]
          text=text.lower()
          print(user_id, text)

          if text.lower() == 'привет':

              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Привет! Я  - Харитоша, я - бот, который хочет, чтобы у тебя появилось больше приятных друзей :)''',
                                           "random_id": int(r.uniform(0, 2 ** 32))})
              if user_id not in people:  # заносим человека в базу опросников
                  #people[user_id] = ''

                  status[user_id] = 10
                  days_of_week[user_id] = ''
                  vk.method("messages.send", {"peer_id": user_id, "message": '''Я хочу получше узнать тебя, ответь мне, пожалуйста, на пару вопросов.
                  Скажи, для начала, тебе неважно о чем разговаривать?''',"keyboard": create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              else:
                  vk.method("messages.send", {"peer_id": user_id, "message": '''привет''',
                                              "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})


          elif (text.lower() == "да") and (status[user_id] == 10):  # если ответ да
              people[user_id] = '1,0,0,0'
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Ну вот, славно поговорили, зови, если что''',
                                          'keyboard': functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              

          elif ((text.lower() == 'нет') and (status[user_id] == 10)):  # если ответ нет
              people[user_id] = '0,'
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично, а любишь ли ты спорт?''',
                                          "keyboard": create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 15

          elif (text.lower() == "да") and (status[user_id] == 15):  # если ответ да
              people[user_id] += '1,'
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''А ты любишь музыку?''',
                                          'keyboard': create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 1

          elif ((text.lower() == 'нет') and (status[user_id] == 15)):  # если ответ нет
              people[user_id] += '0,'
              vk.method("messages.send", {"peer_id": user_id, "message": '''А ты любишь музыку?''',
                                          "keyboard": create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 1



          elif ((text.lower() == 'да') and (status[user_id] == 1)):
              people[user_id] +='1,'
              status[user_id] = 2
              vk.method("messages.send", {"peer_id": user_id, "message": '''Знаешь, обычно люди любят смотреть фильмы, а затем обсуждать их.
            А как ты относишься к киноискусству? Любишь фильмы? Я могу посоветовать тебе парочку после опросика''',
                                          "keyboard": create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})


          elif ((text.lower() == 'нет') and (status[user_id] == 1)):
              people[user_id] +='0,'
              status[user_id] = 2
              vk.method("messages.send", {"peer_id": user_id, "message": '''Знаешь, обычно люди любят смотреть фильмы, а затем обсуждать их.
            А как ты относишься к киноискусству? Любишь фильмы? Я могу посоветовать тебе парочку после опросика''',
                                          "keyboard": create_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})



          elif ((text.lower() == 'да') and (status[user_id] == 2)):
              print(1)
              people[user_id] += '1'
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Ну вот, славно поговорили, зови, если что''',
                                          'keyboard': functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5

          elif ((text.lower() == 'нет') and (status[user_id] == 2)):
              people[user_id] += '0'
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Ну вот, славно поговорили, зови, если что''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              print(people[user_id])
              status[user_id] = 5

          ### все еще определение дня недели###

          elif ((text.lower() == 'понедельник') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})

              status[user_id] = 5
              days_of_week[user_id] = 1
              pp+=1

          elif ((text.lower() == 'вторник') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              print(status[user_id])
              days_of_week[user_id] = 2
              pp+=1

          elif ((text.lower() == 'среда') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              days_of_week[user_id] = 3
              pp+=1

          elif ((text.lower() == 'четверг') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              days_of_week[user_id] = 4
              pp+=1


          elif ((text.lower() == 'пятница') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              days_of_week[user_id] = 5
              pp+=1

          elif ((text.lower() == 'суббота') and (status[user_id] == 6)):
              vk.method("messages.send", {"peer_id": user_id, "message": '''Отлично! Тогда перед обедом я сообщу тебе к какому столику тебе подходить''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              status[user_id] = 5
              days_of_week[user_id] = 6
              pp+=1


          elif ((text.lower() == 'что тут вообще происходит?') and (status[user_id] == 5)):
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Я - Харитоша, бот по знакомству людей. Когда мы с тобой разговаривали, я узнал твои интересы.''',
                                          "random_id": int(r.uniform(0, 2 ** 32))})

              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Напиши мне "хочу свиданку", и я подберу тебе приятного собеседника''',
                                          "random_id": int(r.uniform(0, 2 ** 32))})

              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Если ты хочешь посмотреть/почитать что-то интересное напиши мне "хочу фильм"/"хочу книгу" ''',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})





          elif ((text.lower() == 'хочу свиданку') and (status[user_id] == 5) and (user_id not in people_today)):

              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Укажи, пж, день недели в который ты хотел бы встретится c кем-то''',
                                          "keyboard": days_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})
              people_today.append(user_id)
              print(people_today)
              print(days_of_week)
              status[user_id] =6

          elif ((text.lower() == 'хочу свиданку') and (user_id in people_today)):
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": 'Ты уже записался на какой-то день недели еще раз сможешь записаться когда сходишь на свидание',
                                          "keyboard": functional_keyboard(), "random_id": int(r.uniform(0, 2 ** 32))})


          else:
              vk.method("messages.send", {"peer_id": user_id,
                                          "message": '''Чувак, ты написал что-то не то, но мой создатель тупой и не знает как это пофиксить''',
                                          "random_id": int(r.uniform(0, 2 ** 32))})

      #schedule.run_pending()
