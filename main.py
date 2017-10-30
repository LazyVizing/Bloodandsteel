import telebot
import Token
import time
from telebot import types
import random

bot = telebot.TeleBot(Token.token)

# Это какой-то пиздец. Что я пишу. Ебанный свет. Ебните просто эту клаву нухуй.
# bot.send_message(281311373, 'test')

# upd = bot.get_updates()
# print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())


class Main:
    @bot.message_handler(commands=['start'])
    def handle_text(message):
        bot.send_message(message.chat.id, ''' Ночной лес. Как много тайн хранит его чаща. Свежа еще в вашей памяти 
недавняя битва, проходившая средь этих древних деревьев.Кое где все- еще лежат не обглоданные трупы павших солдат. 
Видно даже диким зверям, если они и остались после гегемонии немецкой боевой мощи в этих землях, не справиться с 
остатками этих тел.Вы старательно пытаетесь думать как можно больше, чтобы вытеснить мысли о холоде, проникающем в 
каждую клетку вашего тела.Быть может удача окончательно оставила меня"- регулярно проносилось в подсознании. Так бы 
вашему телу и остаться погребенным в снегу, если бы не огонек, замелькавший в километре.Утопая в снегу, теряя самого 
себя в этой темноте, жизнь поддерживала лишь мысль о спасении от холодной смерти. Не важно, кто ждал возле того огня, 
быть может это лишь приманка, но подобные мысли успешно изгонялись из головы.Ввалившись в сторожку, словно моля о 
секунде около огня, вы заметили обитателя. Старика. Седая борода, лицо полное морщин и истощавшее тело. Он помог вам 
подняться, напоил чаем и накормил горячей похлебкой.Можешь ли ты мне рассказать что-нибудь о себе? ''')  #Эту тему нужно переписать

        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Солдат')
        user_markup.row('Фермер')
        user_markup.row('Бродяга')
        bot.send_message(message.chat.id, 'Так откуда ты?', reply_markup=user_markup)

    @bot.message_handler(commands=['Солдат'])
    def handle_text(message):
        bot.send_message(message.chat.id, '''- "Я обычный солдат, бежавший из свой роты несколько месяцев назад. 
        Я почувствовал как война окончательно уничтожает остатки человеческого во мне. Еще до войны я учился в старинном 
        университете Австро-Венгрии.Я учился созидать. Я учился творить. Мое воображение завораживали величейшие достояния 
        мировой культуры. Только представь,старик, что бы я мог создать,если бы не пришла эта чертова война. Из созидателя я 
        превратился в несущего смерть. Творец внутри умер, а на его месте родилась машина для выполнения приказов. Даже если бы 
        и выжил в этой мясорубки,не думаю что смог бы взглянуть в зеркало. Кто я теперь? Лишь тень былого себя..."
            Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
        ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''') #И эту тему тоже
        keyboard = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id,
                         "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                         reply_markup=keyboard)

    @bot.message_handler(commands=['Фермер'])
    def handle_text(message):
        bot.send_message(message.chat.id, '''-"Я был обычным фермером. Поколениями моя семья трудилась на полях 
        великой Австро-Венгрии. Вы не поверите, но 4 года назад, когда сам император проезжал по нашим землям, остановился
        возле поля ржи, на котором тогда я трудился с семьей, да одобрительно так окинул взором нашу работу.Жаркие труды на 
        полях, сменялись холодными зимними вечерами в кругу семьи. Матушка всегда готовила отменный тирольский суп.А как подрос,
        собирался жениться да детей нарожать. Даже нашел себе суженную. Но этим планам не удалось сбыться, эта война отняла у 
        меня все: похоронила мою семью, сожгла поля и искромсала мою душу на корню. Теперь я бегу все дальше и дальше. Не знаю 
        куда. Просто бегу."
            Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
        ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''')
        keyboard = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id,
                         "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                         reply_markup=keyboard)

    @bot.message_handler(commands=['Бродяга'])
    def handle_text(message):
        bot.send_message(message.chat.id, ''' -"Я просто бродяга. Сколько себя помню, я всегда скитался по миру. 
        Родителей потерял когда мне было лет 7. Не помню точно. Когда бегал с какими- то мальчишками в детстве, частенько 
        слышал истории о том, что родители заставляют их делать то, что им не нравится. А у меня была лишь одна мысль- не 
        понимаете вы своего счастья. Взрослел я в мародерстве и разбоях. Горжусь или же стыжусь я этого? Однозначно нет. 
        Я просто старался выжить в этом мире. А потом пришла война. Кругом люди теряли все в один момент и учились жить в новом 
        мире: без еды, крыши над головой и совершенно одни. Это был мой мир."
            Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
        ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''')
        keyboard = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, 'Команда "/help" откроет все доступные команды')
        bot.send_message(message.chat.id,
                         "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                         reply_markup=keyboard)

    @bot.message_handler(commands=['help'])
    def handle_text(message):
        bot.send_message(message.chat.id, '/stat - Вызов контекстного меню')


class Mono(Main):
    health = 100
    level = 1
    global knife
    global rifle
    global pistol
    global bullrif
    global bullpistol
    global knifeecip
    global rifleecip
    global pistolecip
    global standartdmg
    global knifedmg
    global rifledmg
    global pistoldmg
    global riflebar
    global pistolbar
    global botl
    global enemy1
    global enemy2
    global enemy3
    global enemy4
    global enemy5
    global enemy1dmg
    global enemy2dmg
    global enemy3dmg
    global enemy4dmg
    global enemy5dmg
    global enemy1hp
    global enemy2hp
    global enemy3hp
    global enemy4hp
    global enemy5hp
    global turn
    global slol
    global enemycount
    global money


    def __init__(self, knife=0, rifle=0, pistol=0, bullrif=0, bullpistol=0, knifeecip=0, rifleecip = 0, pistolecip = 0 , standartdmg=5, knifedmg = 12, rifledmg = 24, pistoldmg = 17, riflebar = 12, pistolbar = 16, botl = 0, enemy1dmg=6,
                 enemy2dmg=20, enemy3dmg=24, enemy4dmg=35, enemy5dmg=60, enemy1hp=12, enemy2hp=16, enemy3hp=27,
                 enemy4hp=34, enemy5hp=47, money=0):
        self.knife = knife
        self.rifle = rifle
        self.pistol = pistol
        self.bullrif = bullrif
        self.bullpistol = bullpistol
        self.knifeecip = knifeecip
        self.rifleecip = rifleecip
        self.pistolecip = pistolecip
        self.standartdmg = standartdmg
        self.knifedmg = knifedmg
        self.rifledmg = rifledmg
        self.pistoldmg = pistoldmg
        self.riflebar = riflebar
        self.pistolbar = pistolbar
        self.botl = botl
        self.enemy1dmg = enemy1dmg
        self.enemy2dmg = enemy2dmg
        self.enemy3dmg = enemy3dmg
        self.enemy4dmg = enemy4dmg
        self.enemy5dmg = enemy5dmg
        self.enemy1hp = enemy1hp
        self.enemy2hp = enemy2hp
        self.enemy3hp = enemy3hp
        self.enemy4hp = enemy4hp
        self.enemy5hp = enemy5hp
        self.money = money


    @bot.message_handler(commands=['stat'])
    def handle_status(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Локация')
        user_markup.row('Статус')
        user_markup.row('Инвентарь')
        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)

    @bot.message_handler(commands=['knife'])
    def handle_status(message):
        global knifeecip
        global knife
        if knifeecip == 0:
            bot.send_message(message.chat.id,
                             'Вы экипировали нож. Ваш урон в ближнем бою: ' + str(int(standartdmg) + int(knifedmg)))
            knife -= 1
            knifeecip += 1

        if knifeecip > 0:
            bot.send_message(message.chat.id, 'Вы уже экипировали нож')

    @bot.message_handler(commands=['pistol'])
    def handle_status(message):
        global pistolecip
        global pistol
        if pistolecip == 0:
            bot.send_message(message.chat.id,
                             'Вы экипировали пистолет. Урон с пистолета: ' + str(int(pistoldmg)))
            pistol -= 1
            pistolecip += 1

        if pistolecip > 0:
            bot.send_message(message.chat.id, 'Вы уже экипировали пистолет')

    @bot.message_handler(commands=['rifle'])
    def handle_status(message):
        global rifleecip
        global rifle
        if rifleecip == 0:
            bot.send_message(message.chat.id,
                             'Вы экипировали винтовку. Урон винтовки: ' + str(int(rifledmg)))
            rifle -= 1
            rifleecip += 1

        if rifleecip > 0:
            bot.send_message(message.chat.id, 'Вы уже экипировали нож')

    @bot.message_handler(commands=['botl'])
    def handle_status(message):
        global botl
        global health
        bot.send_message(message.chat.id,
                         'Вы восстановили 10 единиц здоровья. Ваш уровень здоровья: ' + str(ild.health + int(10)))
        ild.health = ild.health + 10
        botl -= 1
        return  ild.health

    @bot.message_handler(commands=['Fight'])
    def handle_text(message):
        global turn
        turn = 1
        global enemy
        enemy = random.randint(1, 4)
        global enemycount
        enemycount = random.randint(1, 3)
        if enemy == 1:
            bot.send_message(message.chat.id, 'Вам посвстречались ' + str(enemycount) + ' ' + str(enemy1))

            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Удар вблизи')
            user_markup.row('Выстрел из пистолета')
            user_markup.row('Выстрел из винтовки')
            bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
        if enemy == 2:
            bot.send_message(message.chat.id, 'Вам посвстречались ' + str(enemycount) + ' ' + str(enemy2))

            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Рукопашная')
            user_markup.row('Использовать пистолет')
            user_markup.row('Использовать винтовку')
            bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
        if enemy == 3:
            bot.send_message(message.chat.id, 'Вам посвстречались ' + str(enemycount) + ' ' + str(enemy2))

            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Ближний бой')
            user_markup.row('Выстрелить из винтовки')
            user_markup.row('Выстрелить из пистолета')
            bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
        if enemy == 4:
            bot.send_message(message.chat.id, 'Вам посвстречались ' + str(enemycount) + ' ' + str(enemy2))

            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Попровобать вблизи')
            user_markup.row('Попробовать из пистолета')
            user_markup.row('Попробовать из винтовки ')
            bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)

    @bot.message_handler(commands=['Run'])
    def handle_text(message):
        s = random.randint(1, 14)
        if s > 12:
            bot.send_message(message.chat.id, 'Вы успешно сбежали.')
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('Локация')
            user_markup.row('Статус')
            user_markup.row('Инвентарь')
            bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
        if s < 13:
            bot.send_message(message.chat.id, 'Вам не удалось сбежать')
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/Fight')
            bot.send_message(message.chat.id, 'Теперь остается только биться', reply_markup=user_markup)




    def set(self, health, level):
        self.health = health
        self.level = level

    @bot.message_handler(commands=['Left'])
    def handle_text(message):
        b = 0

        while b == 0:
            global money
            hod = random.randint(7, 27)
            i = random.randint(3, 24)
            h = random.randint(1, 4)
            R = random.randint(1, 4)
            global bullrif
            global bullpistol
            c = random.randint(10, 15)
            g = random.randint(10, 15)
            if 3 < i <= 5:
                bot.send_message(message.chat.id, 'С вами ничего не произошло ')

            if 5 < i <= 10:
                bot.send_message(message.chat.id, 'Вам повстречались противники ')

                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('/Fight')
                user_markup.row('/Run')
                bot.send_message(message.chat.id, 'Начнешь бой или попробовуешь сбежать?', reply_markup=user_markup)

            if 10 < i <= 15:
                bot.send_message(message.chat.id, 'Вы заразились ересью и потеряли ' + str(h) + ' единицы здоровья')
                ild.health -= h

            if 15 < i <= 20:
                bot.send_message(message.chat.id, 'Лутец ')
                if R == 1:
                    fga = random.randint(10, 14)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 2:
                    fga = random.randint(20, 35)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 3:
                    fga = random.randint(100, 120)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R ==4:
                    bot.send_message(message.chat.id, 'Вы получили патронов для пистолета ' + str(c) + ' и винтовки ' + str(g))

                    bullpistol += c
                    bullrif += g
                if R == 5:
                    randboil = random.randint(1, 3)
                    bot.send_message(message.chat.id,
                                     'Вы получили ' + str(randboil) + 'медицинских аптечек')
                    global botl
                    botl = botl + randboil
                if R == 6:
                    bot.send_message(message.chat.id,
                                     'Вы получили пистолет')
                    global pistol
                    pistol += 1
                if R == 7:
                    bot.send_message(message.chat.id,
                                     'Вы получили винтовку')
                    global rifle
                    rifle += 1
                if R == 8:
                    bot.send_message(message.chat.id,
                                     'Вы получили нож')
                    global knife
                    knife += 1


            if 20 < i <= 27:
                bot.send_message(message.chat.id, 'Вы нашли магазинчик. Откуда магазинчик в лабиринте? Да я понятия не имею. Но он пока закрыт, так что горите. ')




            if hod == 0:
                bot.send_message(message.chat.id, 'Вы достигли пункта назначения ')
            return None

    @bot.message_handler(commands=['Directly'])
    def handle_text(message):
        b = 0

        while b == 0:
            global money
            hod = random.randint(7, 27)
            i = random.randint(3, 24)
            h = random.randint(1, 4)
            R = random.randint(1, 4)
            global bullrif
            global bullpistol
            c = random.randint(10, 15)
            g = random.randint(10, 15)
            if 3 < i <= 5:
                bot.send_message(message.chat.id, 'С вами ничего не произошло ')

            if 5 < i <= 10:
                bot.send_message(message.chat.id, 'Вам повстречались противники ')

                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('/Fight')
                user_markup.row('/Run')
                bot.send_message(message.chat.id, 'Начнешь бой или попробовуешь сбежать?', reply_markup=user_markup)

            if 10 < i <= 15:
                bot.send_message(message.chat.id, 'Вы заразились ересью и потеряли ' + str(h) + ' единицы здоровья')
                ild.health -= h

            if 15 < i <= 20:
                bot.send_message(message.chat.id, 'Лутец ')
                if R == 1:
                    fga = random.randint(10, 14)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 2:
                    fga = random.randint(20, 35)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 3:
                    fga = random.randint(100, 120)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R ==4:
                    bot.send_message(message.chat.id, 'Вы получили патронов для пистолета ' + str(c) + ' и винтовки ' + str(g))

                    bullpistol += c
                    bullrif += g
                if R == 5:
                    randboil = random.randint(1, 3)
                    bot.send_message(message.chat.id,
                                     'Вы получили ' + str(randboil) + 'медицинских аптечек')
                    global botl
                    botl = botl + randboil
                if R == 6:
                    bot.send_message(message.chat.id,
                                     'Вы получили пистолет')
                    global pistol
                    pistol += 1
                if R == 7:
                    bot.send_message(message.chat.id,
                                     'Вы получили винтовку')
                    global rifle
                    rifle += 1
                if R == 8:
                    bot.send_message(message.chat.id,
                                     'Вы получили нож')
                    global knife
                    knife += 1


            if 20 < i <= 27:
                bot.send_message(message.chat.id, 'Вы нашли магазинчик. Откуда магазинчик в лабиринте? Да я понятия не имею. Но он пока закрыт, так что горите. ')



            if hod == 0:
                bot.send_message(message.chat.id, 'Вы достигли пункта назначения ')
            return None

    @bot.message_handler(commands=['Rigth'])
    def handle_text(message):
        b = 0

        while b == 0:
            global money
            hod = random.randint(7, 27)
            i = random.randint(3, 24)
            h = random.randint(1, 4)
            R = random.randint(1, 4)
            global bullrif
            global bullpistol
            c = random.randint(10, 15)
            g = random.randint(10, 15)
            if 3 < i <= 5:
                bot.send_message(message.chat.id, 'С вами ничего не произошло ')

            if 5 < i <= 10:
                bot.send_message(message.chat.id, 'Вам повстречались противники ')

                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('/Fight')
                user_markup.row('/Run')
                bot.send_message(message.chat.id, 'Начнешь бой или попробовуешь сбежать?', reply_markup=user_markup)

            if 10 < i <= 15:
                bot.send_message(message.chat.id, 'Вы заразились ересью и потеряли ' + str(h) + ' единицы здоровья')
                ild.health -= h

            if 15 < i <= 20:
                bot.send_message(message.chat.id, 'Лутец ')
                if R == 1:
                    fga = random.randint(10, 14)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 2:
                    fga = random.randint(20, 35)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R == 3:
                    fga = random.randint(100, 120)
                    bot.send_message(message.chat.id, 'Вы получили ' + str(fga) + ' золота')
                    money = money + fga
                if R ==4:
                    bot.send_message(message.chat.id, 'Вы получили патронов для пистолета ' + str(c) + ' и винтовки ' + str(g))

                    bullpistol += c
                    bullrif += g
                if R == 5:
                    randboil = random.randint(1, 3)
                    bot.send_message(message.chat.id,
                                     'Вы получили ' + str(randboil) + 'медицинских аптечек')
                    global botl
                    botl = botl + randboil
                if R == 6:
                    bot.send_message(message.chat.id,
                                     'Вы получили пистолет')
                    global pistol
                    pistol += 1
                if R == 7:
                    bot.send_message(message.chat.id,
                                     'Вы получили винтовку')
                    global rifle
                    rifle += 1
                if R == 8:
                    bot.send_message(message.chat.id,
                                     'Вы получили нож')
                    global knife
                    knife += 1


            if 20 < i <= 27:
                bot.send_message(message.chat.id, 'Вы нашли магазинчик. Откуда магазинчик в лабиринте? Да я понятия не имею. Но он пока закрыт, так что горите. ')



            if hod == 0:
                bot.send_message(message.chat.id, 'Вы достигли пункта назначения ')
            return None

    @bot.message_handler(commands=['Fight'])
    def handle_text(message):
        keyboard = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Начать битву ", callback_data="Fight")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id,
                         "/Fight",
                         reply_markup=keyboard)

    @bot.message_handler(commands=['Run'])
    def handle_text(message):
        if R > 4:
            bot.send_message(message.chat.id, 'Вам не удалось сбежать ')
        else:
            bot.send_message(message.chat.id, 'Вам удалось сбежать. На этот раз... ')

            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/Left ')
            user_markup.row('/Directly')
            user_markup.row('/Rigth')
            bot.send_message(message.chat.id, 'Куда держим путь?', reply_markup=user_markup)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        global money
        if message.text == 'Статус':
            bot.send_message(message.chat.id,
                             'Ваш уровень здоровья: ' + str(ild.health) + '  Ваш уровень: ' + str(ild.level) + '  Количество золота: ' + str(money))
        if message.text == 'Локация':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/Left ')
            user_markup.row('/Directly')
            user_markup.row('/Rigth')
            user_markup.row('/stat')
            bot.send_message(message.chat.id, 'Куда держим путь?', reply_markup=user_markup)
        if message.text == 'Инвентарь':

            if knife > 0:
                bot.send_message(message.chat.id,
                                 'Количество ножей в вашей сумке: ' + str(knife) + '     /knife - экипировать нож.')

            if rifle > 0:
                bot.send_message(message.chat.id,
                                 'Количество винтовок в вашей сумке: ' + str(rifle) + '  /rifle - экипировать винтовку')

            if pistol > 0:
                bot.send_message(message.chat.id,
                                 "Количество пистолетов в вашей сумке: " + str(pistol) + '   /pistol - экипировать '
                                                                                         'пистолет')
            if bullrif > 0:
                bot.send_message(message.chat.id,
                                 'Патронов для винтовки: ' + str(bullrif))
            if bullpistol > 0:
                bot.send_message(message.chat.id,
                                 'Патронов для пистолета: ' + str(bullpistol))
            if botl > 0:
                bot.send_message(message.chat.id,
                                 'Медицинских аптечек: ' + str(botl) + '   /botl - исцилиться')
            if money > 0:
                bot.send_message(message.chat.id,
                                 'Золота у вас: ' + str(money))

        if message.text == 'Удар вблизи':
            global enemy
            global slol
            global enemycount
            global enemy1hp


            enemycount = random.randint(1, 4)
            bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy1) + ' ' + str(standartdmg) + ' урона')
            enemy1hp = enemy1hp - standartdmg
            bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy1hp)) + ' очков здоровья')
            slol = 0
            if slol == 1:
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Удар вблизи')
                user_markup.row('Выстрел из пистолета')
                user_markup.row('Выстрел из винтовки')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                if enemy1hp > 0:
                    slol -= 1
                if enemy1hp < 0:
                    slol += 2


            if slol == 0:
                enemy1dmg = 6
                bot.send_message(message.chat.id,
                                             'Противник нанес вам ' + str(int(enemy1dmg)) + ' урона')

                ild.health = ild.health - enemy1dmg

                if enemy1hp > 0:
                    slol += 1
                if enemy1hp < 0:
                    slol += 3
                if ild.health < 1:
                    slol += 4



            if enemy1hp < 1:
                fga = random.randint(1, 5)
                bot.send_message(message.chat.id, 'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                money = money + fga
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return money
            if ild.health < 2:
                bot.send_message(message.chat.id, 'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                global health
                ild.health = 1
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return ild.health

        if message.text == 'Выстрел из винтовки':

            global riflebar
            global rifleecip
            if rifleecip == 0:
                bot.send_message(message.chat.id, 'У вас нет винтовки')
            elif rifleecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy1) + ' ' + str(rifledmg) + ' урона')
                enemy1hp = enemy1hp - rifledmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy1hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине винтовки осталось: ' + str(riflebar) + ' патронов')
                riflebar -= 1
                slol = 0

                if riflebar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if riflebar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy1hp > 0:
                            slol -= 1
                        if enemy1hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy1dmg = 6
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy1dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy1hp > 0:
                            slol += 1
                        if enemy1hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy1hp < 1:
                        fga = random.randint(1, 3)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Выстрел из пистолета':
            global pistolbar
            global pistolecip
            if pistolecip == 0:
                bot.send_message(message.chat.id, 'У вас нет пистолета ')
            elif pistolecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy1) + ' ' + str(pistoldmg) + ' урона')
                enemy1hp = enemy1hp - pistoldmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy1hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине пистолета осталось: ' + str(pistolbar) + ' патронов')
                pistolbar -= 1
                slol = 0

                if pistolbar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if pistolbar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy1hp > 0:
                            slol -= 1
                        if enemy1hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy1dmg = 6
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy1dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy1hp > 0:
                            slol += 1
                        if enemy1hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy1hp < 1:
                        fga = random.randint(1, 3)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Рукопашная':
            global enemy


            global enemy2hp
            enemycount = random.randint(1, 4)
            bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy2) + ' ' + str(standartdmg) + ' урона')
            enemy2hp = enemy2hp - standartdmg
            bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy2hp)) + ' очков здоровья')
            slol = 0
            if slol == 1:
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Удар вблизи')
                user_markup.row('Выстрел из пистолета')
                user_markup.row('Выстрел из винтовки')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                if enemy2hp > 0:
                    slol -= 1
                if enemy2hp < 0:
                    slol += 2


            if slol == 0:
                enemy2dmg = 20
                bot.send_message(message.chat.id,
                                             'Противник нанес вам ' + str(int(enemy2dmg)) + ' урона')

                ild.health = ild.health - enemy2dmg

                if enemy2hp > 0:
                    slol += 1
                if enemy2hp < 0:
                    slol += 3
                if ild.health < 1:
                    slol += 4



            if enemy2hp < 1:
                fga = random.randint(6, 11)
                bot.send_message(message.chat.id,
                                 'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                money = money + fga
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return money
            if ild.health < 2:
                bot.send_message(message.chat.id, 'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                global health
                ild.health =1
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return ild.health


        if message.text == 'Использовать винтовку':

            if rifleecip == 0:
                bot.send_message(message.chat.id, 'У вас нет винтовки')
            elif rifleecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy2) + ' ' + str(rifledmg) + ' урона')
                enemy2hp = enemy2hp - rifledmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy2hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине винтовки осталось: ' + str(riflebar) + ' патронов')
                riflebar -= 1
                slol = 0

                if riflebar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if riflebar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy2hp > 0:
                            slol -= 1
                        if enemy2hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy2dmg = 6
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy1dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy2hp > 0:
                            slol += 1
                        if enemy2hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy2hp < 1:
                        fga = random.randint(6, 11)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                        return gold
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Использовать пистолет':

            if pistolecip == 0:
                bot.send_message(message.chat.id, 'У вас нет пистолета ')
            elif pistolecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy2) + ' ' + str(pistoldmg) + ' урона')
                enemy2hp = enemy2hp - pistoldmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy2hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине пистолета осталось: ' + str(pistolbar) + ' патронов')
                pistolbar -= 1
                slol = 0

                if pistolbar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if pistolbar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy2hp > 0:
                            slol -= 1
                        if enemy2hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy2dmg = 20
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy2dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy2hp > 0:
                            slol += 1
                        if enemy2hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy2hp < 1:
                        fga = random.randint(6, 11)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Ближний бой':
            global enemy


            global enemy3hp
            enemycount = random.randint(1, 4)
            bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy3) + ' ' + str(standartdmg) + ' урона')
            enemy3hp = enemy3hp - standartdmg
            bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy3hp)) + ' очков здоровья')
            slol = 0
            if slol == 1:
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Удар вблизи')
                user_markup.row('Выстрел из пистолета')
                user_markup.row('Выстрел из винтовки')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                if enemy3hp > 0:
                    slol -= 1
                if enemy3hp < 0:
                    slol += 2


            if slol == 0:
                enemy3dmg = 24
                bot.send_message(message.chat.id,
                                             'Противник нанес вам ' + str(int(enemy3dmg)) + ' урона')

                ild.health = ild.health - enemy3dmg

                if enemy3hp > 0:
                    slol += 1
                if enemy3hp < 0:
                    slol += 3
                if ild.health < 1:
                    slol += 4



            if enemy3hp < 1:
                fga = random.randint(15, 20)
                bot.send_message(message.chat.id,
                                 'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                money = money + fga
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return money

            if ild.health < 2:
                bot.send_message(message.chat.id, 'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                global health
                ild.health = 1
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return ild.health

        if message.text == 'Выстрелить из винтовки':


            if rifleecip == 0:
                bot.send_message(message.chat.id, 'У вас нет винтовки')
            elif rifleecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy3) + ' ' + str(rifledmg) + ' урона')
                enemy3hp = enemy3hp - rifledmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy3hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине винтовки осталось: ' + str(riflebar) + ' патронов')
                riflebar -= 1
                slol = 0

                if riflebar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if riflebar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy3hp > 0:
                            slol -= 1
                        if enemy3hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy3dmg = 24
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy3dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy3hp > 0:
                            slol += 1
                        if enemy3hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy3hp < 1:
                        fga = random.randint(15, 20)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Выстрелить из пистолета':

            if pistolecip == 0:
                bot.send_message(message.chat.id, 'У вас нет пистолета ')
            elif pistolecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy3) + ' ' + str(pistoldmg) + ' урона')
                enemy3hp = enemy3hp - pistoldmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy3hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине пистолета осталось: ' + str(pistolbar) + ' патронов')
                pistolbar -= 1
                slol = 0

                if pistolbar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if pistolbar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy3hp > 0:
                            slol -= 1
                        if enemy3hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy3dmg = 20
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy3dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy3hp > 0:
                            slol += 1
                        if enemy3hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy3hp < 1:
                        fga = random.randint(15, 20)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Попровобать вблизи':
            global enemy

            global enemy4hp
            enemycount = random.randint(1, 4)
            bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy4) + ' ' + str(standartdmg) + ' урона')
            enemy4hp = enemy4hp - standartdmg
            bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy4hp)) + ' очков здоровья')
            slol = 0
            if slol == 1:
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Удар вблизи')
                user_markup.row('Выстрел из пистолета')
                user_markup.row('Выстрел из винтовки')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                if enemy4hp > 0:
                    slol -= 1
                if enemy4hp < 0:
                    slol += 2


            if slol == 0:
                enemy4dmg = 60
                bot.send_message(message.chat.id,
                                             'Противник нанес вам ' + str(int(enemy4dmg)) + ' урона')

                ild.health = ild.health - enemy1dmg

                if enemy4hp > 0:
                    slol += 1
                if enemy4hp < 0:
                    slol += 3
                if ild.health < 1:
                    slol += 4



            if enemy4hp < 1:
                fga = random.randint(40, 110)
                bot.send_message(message.chat.id,
                                 'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                money = money + fga
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return money
            if ild.health < 2:
                bot.send_message(message.chat.id, 'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                global health
                ild.health =1
                user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                user_markup.row('Локация')
                user_markup.row('Статус')
                user_markup.row('Инвентарь')
                bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                return ild.health

        if message.text == 'Попробовать из винтовки':


            if rifleecip == 0:
                bot.send_message(message.chat.id, 'У вас нет винтовки')
            elif rifleecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy4) + ' ' + str(rifledmg) + ' урона')
                enemy4hp = enemy4hp - rifledmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy4hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине винтовки осталось: ' + str(riflebar) + ' патронов')
                riflebar -= 1
                slol = 0

                if riflebar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if riflebar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy4hp > 0:
                            slol -= 1
                        if enemy4hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy4dmg = 60
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy4dmg)) + ' урона')

                        ild.health = ild.health - enemy4dmg

                        if enemy4hp > 0:
                            slol += 1
                        if enemy4hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy4hp < 1:
                        fga = random.randint(40, 110)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Попробовать из пистолета':

            if pistolecip == 0:
                bot.send_message(message.chat.id, 'У вас нет пистолета ')
            elif pistolecip > 0:
                enemycount = random.randint(1, 4)
                bot.send_message(message.chat.id, 'Вы нанесли ' + str(enemy4) + ' ' + str(pistoldmg) + ' урона')
                enemy4hp = enemy4hp - pistoldmg
                bot.send_message(message.chat.id, 'У противника осталось: ' + str(int(enemy4hp)) + ' очков здоровья')
                bot.send_message(message.chat.id, 'В магазине пистолета осталось: ' + str(pistolbar) + ' патронов')
                pistolbar -= 1
                slol = 0

                if pistolbar == 0:
                    bot.send_message(message.chat.id, 'Вы потратили ход на перезарядку.')
                    riflebar += 12
                    slol -= 1
                if pistolbar > 0:
                    if slol == 1:
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Удар вблизи')
                        user_markup.row('Выстрел из пистолета')
                        user_markup.row('Выстрел из винтовки')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        if enemy4hp > 0:
                            slol -= 1
                        if enemy4hp < 0:
                            slol += 2

                    if slol == 0:
                        enemy4dmg = 60
                        bot.send_message(message.chat.id,
                                         'Противник нанес вам ' + str(int(enemy4dmg)) + ' урона')

                        ild.health = ild.health - enemy1dmg

                        if enemy4hp > 0:
                            slol += 1
                        if enemy4hp < 0:
                            slol += 3
                        if ild.health < 1:
                            slol += 4

                    if enemy4hp < 1:
                        fga = random.randint(40, 110)
                        bot.send_message(message.chat.id,
                                         'Вы победили. У воперженного противника нашлось ' + str(fga) + ' голды')
                        money = money + fga
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return money
                    if ild.health < 2:
                        bot.send_message(message.chat.id,
                                         'Вы проиграли, но добрый разработчик позволит вас продолжить с 1 лском здоровья')
                        global health
                        ild.health = 1
                        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
                        user_markup.row('Локация')
                        user_markup.row('Статус')
                        user_markup.row('Инвентарь')
                        bot.send_message(message.chat.id, 'Контекстное меню вызвано. ', reply_markup=user_markup)
                        return ild.health

        if message.text == 'Солдат':
            bot.send_message(message.chat.id, '''- "Я обычный солдат, бежавший из свой роты несколько месяцев назад. 
Я почувствовал как война окончательно уничтожает остатки человеческого во мне. Еще до войны я учился в старинном 
университете Австро-Венгрии.Я учился созидать. Я учился творить. Мое воображение завораживали величейшие достояния 
мировой культуры. Только представь,старик, что бы я мог создать,если бы не пришла эта чертова война. Из созидателя я 
превратился в несущего смерть. Творец внутри умер, а на его месте родилась машина для выполнения приказов. Даже если бы 
и выжил в этой мясорубки,не думаю что смог бы взглянуть в зеркало. Кто я теперь? Лишь тень былого себя..."
        Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''')  # И эту тему тоже
            keyboard = telebot.types.InlineKeyboardMarkup()
            callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
            keyboard.add(callback_button)
            bot.send_message(message.chat.id,
                             "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                             reply_markup=keyboard)

            fga = random.randint(10, 14)
            money = money + fga

        if message.text == 'Фермер':
            bot.send_message(message.chat.id, '''-"Я был обычным фермером. Поколениями моя семья трудилась на полях 
великой Австро-Венгрии. Вы не поверите, но 4 года назад, когда сам император проезжал по нашим землям, остановился
возле поля ржи, на котором тогда я трудился с семьей, да одобрительно так окинул взором нашу работу.Жаркие труды на 
полях, сменялись холодными зимними вечерами в кругу семьи. Матушка всегда готовила отменный тирольский суп.А как подрос,
собирался жениться да детей нарожать. Даже нашел себе суженную. Но этим планам не удалось сбыться, эта война отняла у 
меня все: похоронила мою семью, сожгла поля и искромсала мою душу на корню. Теперь я бегу все дальше и дальше. Не знаю 
куда. Просто бегу."
        Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''')
            keyboard = telebot.types.InlineKeyboardMarkup()
            callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
            keyboard.add(callback_button)
            bot.send_message(message.chat.id,
                             "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                             reply_markup=keyboard)

            fga = random.randint(5, 8)
            money = money + fga

        if message.text == 'Бродяга':
            bot.send_message(message.chat.id, ''' -"Я просто бродяга. Сколько себя помню, я всегда скитался по миру. 
Родителей потерял когда мне было лет 7. Не помню точно. Когда бегал с какими- то мальчишками в детстве, частенько 
слышал истории о том, что родители заставляют их делать то, что им не нравится. А у меня была лишь одна мысль- не 
понимаете вы своего счастья. Взрослел я в мародерстве и разбоях. Горжусь или же стыжусь я этого? Однозначно нет. 
Я просто старался выжить в этом мире. А потом пришла война. Кругом люди теряли все в один момент и учились жить в новом 
мире: без еды, крыши над головой и совершенно одни. Это был мой мир."
        Скупая слеза скатилась по щеке юноши. Не рискнул старик больше донимать собеседника, дал ему закончить
ужин и приготовился ко сну. С утра,наколов дров для старца, юноша пустился в свой долгий путь по подземельям...''')
            keyboard = telebot.types.InlineKeyboardMarkup()
            callback_button = telebot.types.InlineKeyboardButton(text="Нажмите на команду выше. ", callback_data="dest")
            keyboard.add(callback_button)
            bot.send_message(message.chat.id, 'Команда "/help" откроет все доступные команды')
            bot.send_message(message.chat.id,
                             "Каждый раз как захотите вызвать контекстное меню, вводите эту команду. /stat",
                             reply_markup=keyboard)

            fga = random.randint(1, 5)
            money = money + fga


knife = 0
rifle = 0
pistol = 0
bullrif = 0
bullpistol = 0
knifeecip = 0
rifleecip = 0
pistolecip = 0
standartdmg = 5
knifedmg = 12
pistoldmg = 17
rifledmg = 24
riflebar = 12
pistolbar = 16
botl = 0

R = random.randint(1, 5)
ild = Mono()
ild.set(120, 1)

enemy1 = str('Паук-мутант из нижнего Урюпинска')
enemy2 = str('Солдат с автоматом')
enemy3 = str('Механизированный дед')
enemy4 = str('Огромная махина смерти')
enemy5 = str('Василий Петрович')
enemy1dmg = 6
enemy2dmg = 20
enemy3dmg = 24
enemy4dmg = 35
enemy5dmg = 60
enemy1hp = 12
enemy2hp = 16
enemy3hp = 27
enemy4hp = 34
enemy5hp = 47
turn = 0
enemycount = 0
money = 0

bot.polling(none_stop=True, interval=3)
