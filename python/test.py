import re

s = "Иван Иванович! Нужен ответ на письмо от pizda@fuck_ru ivanoff@ivan-chai.ru. Не забудьте поставить в копию serge'o-lupin@mail.ru - это важно."

print(re.findall(r"(\b(?:\w+[A-Za-z]|[+-_.']|[A-Za-z])+@(?:\w+[A-Za-z]|[+-.']|[A-Za-z])+)\b", s))

#привет
#текст до собаки (64 латинских букв и цифр и символов),
#который включает символы ('._+-)  @  
# текст для домена (255 латинских букв, цифр)
# ни local-part ни domain-part не начинаются и не заканчиваются на .+-
# в адресе должна быть одна точка.

#(:?\w+)
#/w+[0-9A-Za-z]['._+-][0-9A-Za-z][-@])