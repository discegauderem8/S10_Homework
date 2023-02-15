from aiogram import Bot, Dispatcher, executor, types
import game

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Введите команду /start, чтобы начать игру.\n"
                        f"Вначале следуйте инструкции, далее вводите ответ, нажав на соответствующую кнопку")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Здравствуй, {name}! Сыграем в игру, где надо по очереди брать конфеты,\n"
                        f"а забравший их последним выигрывает. Введи через пробел сначала общее \n"
                        f"число конфет, а затем максимум, который можно взять за раз (max - 9)")

    @dp.message_handler()
    async def initialise_game(message: types.Message):
        data = message.text.split()
        await message.answer(f"{game.first_computer_move(int(data[0]), int(data[1]))},\n"
                             f"сколько конфет ты возьмешь за этот ход? (введи число)", reply_markup=keyboard)

        @dp.callback_query_handler(lambda c: True)
        async def callback_handler(query):
            data = query.data
            if data == "1":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "2":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "3":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "4":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "5":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "6":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "7":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "8":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "9":
                await message.answer(text=f"{game.other_computer_moves(int(data))}", reply_markup=keyboard)
            if data == "0":
                await bot.send_photo(chat_id=message.from_user.id, photo = "https://million-wallpapers.ru/wallpapers/5/26/518096185101510/ves-lyj-robot-lezhit-na-polu.jpg", caption="Спасибо за игру!", reply_markup=types.ReplyKeyboardRemove())

keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard.row(types.InlineKeyboardButton("1", callback_data="1"),
             types.InlineKeyboardButton("2", callback_data="2"),
             types.InlineKeyboardButton("3", callback_data="3"))
keyboard.row(types.InlineKeyboardButton("4", callback_data="4"),
             types.InlineKeyboardButton("5", callback_data="5"),
             types.InlineKeyboardButton("6", callback_data="6"))
keyboard.row(types.InlineKeyboardButton("7", callback_data="7"),
             types.InlineKeyboardButton("8", callback_data="8"),
             types.InlineKeyboardButton("9", callback_data="9"))
keyboard.row(types.InlineKeyboardButton("Закончить игру", callback_data="0"))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
