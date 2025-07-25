from pathlib import Path

BASE_DIR = Path(__file__).parent
MEDIA_URL = BASE_DIR / 'media'

# Пути к файлам
FILE_URL = MEDIA_URL / 'Бар инвентарь.pdf'
FILE_ORDER = MEDIA_URL / 'Создание_Заказа_и_выставление_счёта.pdf'
FILE_CREATE_NUM = MEDIA_URL / 'Создание номенклатуры.pdf'
FILE_RETURN_ORDER = MEDIA_URL / 'Возврат от покупателя.pdf'
FILE_INGREDIENTS = MEDIA_URL / 'Сиропы, топинги, пюре.pdf'
FILE_CREATE_AGENT = MEDIA_URL / 'Создание контрагента.pdf'
FILE_CREATE_OUT_ORDER = MEDIA_URL / 'Создание отгрузочной накладной.pdf'
FILE_ROS = MEDIA_URL / 'Рестинтернешнл.docx'

TEXT_CLEN = """
1. В процессе принятия поставки склад выписывает недостающие/лишние/бракованные товары и записывает его в Яндекс документах 
https://clck.ru/3GMy82 во вкладке «Клён», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» 
в WhatsApp (если есть фото отправляет их в тот же чат).

2. Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\\\srv\\Документы\\Челны Хорека флешка\\Рекламации\\Клен 
путём копирования создает документ в Word, корректирует и сохраняет его в папке 
со следующим порядковым номером рекламации. 
Если есть фото, то вставляет их в папку.

3. Рекламационист отправляет в рекламационный отдел Поставщика 
по почте vellhelp@yandex.ru 
Wordовский документ и имеющиеся фото. 
В теме письма указывается «Рекламация №». Делаем пометку строки в Яндекс таблице 
https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).

4. Ждём ответа от Поставщика не более 5 дней. 
По истечению 5-ти дней, напоминаем отделу рекламаций vellhelp@yandex.ru

5. При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица 
(Цвет всей строки - красный, 
В столбце комментарий указываем причину отказа). 
Просим согласовать руководителя добавить товар в Списание в 1С либо продолжаем доказывать свою точку зрения.

6. При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой. Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку.

7. При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).
"""

TEXT_MASTER_CLASS = """
В процессе принятия поставки склад выписывает недостающие/лишние/ бракованные товары и записывает его в Яндекс документах https://clck.ru/3GMy82 во вкладке «Мастергласс», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» в WhatsApp (если есть фото отправляет их в тот же чат).
Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\Srv\документы\Челны Хорека флешка\Рекламации\Мастергласс путём копирования создает документ в Excel (Например: Акт рекламации №5), корректирует и сохраняет его в папке со следующим порядковым номером рекламации. Если есть фото, то вставляет их в папку. 
Рекламационист отправляет менеджеру Поставщика по почте Смотровой Евгении se@masterglass.ru  Excelевский документ и имеющиеся фото. В теме письма указывается «Рекламация №, дата, артикул». Делаем пометку строки в Яндекс таблице https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).
Ждём ответа от Поставщика не более 5 дней. По истечению 5-ти дней, напоминаем отделу рекламаций se@masterglass.ru  
При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица (Цвет всей строки - красный, В столбце комментарий указываем причину отказа).
При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой. Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку.
При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).
"""

TEXT_PROJECT = """
В процессе принятия поставки склад выписывает недостающие/лишние/ бракованные товары и записывает его в Яндекс документах https://clck.ru/3GMy82 во вкладке «Регион 50», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» в WhatsApp (если есть фото отправляет их в тот же чат).
Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\Srv\документы\Челны Хорека флешка\Рекламации\Регион 50  путём копирования создает новую папку Рекламации (Например: акт рекламации 2). Если есть фото, то вставляет их в папку. 
В поставке к каждой накладной идёт пустой акт рекламации. Заполняем поля: Дата, Место, Получатель, Обнаружено следующее, в табличной части пишем артикул, кол-во, причина, подпись, печать. Сканируем и вставляем скан в папку рекламаций Регион 50. 
Отправляем данный скан на почту Наталье Павловой n.pavlova@project2015.ru  с темой «СРОЧНО! Рекламация №…. , дата, артикул» + вложение фото/видео. Делаем пометку строки в Яндекс таблице https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).
Ждём ответа от Поставщика не более 5 дней. По истечению 5-ти дней, напоминаем отделу рекламаций n.pavlova@project2015.ru 
При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица (Цвет всей строки - красный, В столбце комментарий указываем причину отказа).
При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой. Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку).
При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).
"""

TEXT_RUSSIAN_PROJECT = """
В процессе принятия поставки склад выписывает недостающие/лишние/ бракованные товары и записывает его в Яндекс документах https://clck.ru/3GMy82 во вкладке «Метроном посуда», сообщает о необходимости в написании рекламации в отдельном чате «Рекламации» в WhatsApp (если есть фото отправляет их в тот же чат).
Рекламационист исходя из этого списка по шаблону предыдущих рекламаций \\Srv\документы\Челны Хорека флешка\Рекламации\РП Метроном путём копирования создает документ новую папку для данной рекламации, убирает лишние файлы, редактирует в Word (Например: Рекламация №139), корректирует и сохраняет его. Если есть фото, то вставляет их в папку. 
Рекламационист отправляет менеджеру Поставщика по почте Мельниковой Оксане melnikova-o@rp.ru Wordовский документ и имеющиеся фото. В теме письма указывается «Рекламация №, дата, артикул». Делаем пометку строки в Яндекс таблице https://clck.ru/3GMy82 оранжевым цветом (Ждём ответа).
Ждём ответа от Поставщика не более 5 дней. По истечению 5-ти дней, напоминаем отделу рекламаций melnikova-o@rp.ru 
При Отказе - статус рекламации меняется на Отказ и дополняется Яндекс таблица (Цвет всей строки - красный, В столбце комментарий указываем причину отказа).
При Одобрении - статус рекламации меняется на Согласовано и дополняется Яндекс таблица (Цвет всей строки – желтый, в столбце комментарий указываем необходимый комментарий. Например: должны отправить со следующей поставкой). Предупредить коллег, и проследить, чтобы вложили в следующую отгрузку).
При поступлении товара на склад - статус рекламации меняется на Поступило и дополняется Яндекс таблица (Цвет всей строки – зелёный, в столбце комментарий пишем «Поступило» с указанием даты поступления).
"""
