from collections import defaultdict
import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, RadioField, StringField
from wtforms.validators import DataRequired,EqualTo, ValidationError, InputRequired



COLORS=defaultdict()
COLORS["красный"]=["зеленый", "сине-зеленый", "желтый" , "синий", "черный"]
COLORS["розовый"]=["синий", "бордовый", "серый", "коричневый", "голубой"]
COLORS["оранжевый"]=["фиолетовый", "лиловый", "голубой", "зеленый", "желто-зеленый", "коричневая гамма", "белый цвет"]
COLORS["терракотовый"]=["индиго", "морской волны", "теплый зеленый", "оранжевый", "голубой", "оливковый"]
COLORS["коричневый"]=["оливковый", "золотистый", "серый", "синий", "бежевый"]
COLORS["каштановый"]=["зеленый", "оливковый", "золотистый", "ультрамарин", "цвет резеды", "сиреневый", "серый"]
COLORS["канареечный"]=["зеленовато-желтый", "фиолетовый", "лиловый", "желто-зеленый", "ультрамарин"]
COLORS["золотистый"]=["ультрамарин", "чисто-красный", "темно-зеленый", "небесно-голубой", "пурпурный", "фиолетовый", "темно-золотистый", "оливковый", "коричневый", "серый"]
COLORS["желтый"]=["зеленый", "коричневый", "золотистый"]
COLORS["желто-зеленый"]=["ярко-алый", "коричневый", "киноварный", "фиолетовый", "пурпурный", "синий", "желтовато-зеленый"]
COLORS["оливковый"]=["синий", "коричневый", "серый", "каштановый", "золотистый", "ультрамарин", "зеленовато-синий", "темно-оливковый", "оранжевый", "зеленый", "красный"]
COLORS["травяной"]=["фиолетовый", "пурпурный"]
COLORS["морская волна"]=["кирпичный", "киноварный", "желтый"]
COLORS["бежевый"]=["синий", "коричневый", "красный", "бордо", "каштановый", "ультрамарин", "серый"]
COLORS["голубой"]=["красный", "кирпичный", "киноварный", "ультрамарин", "оранжевый", "пурпурный", "светло-фиолетовый"]
COLORS["ультрамарин"]=["красный", "золотистый", "оранжевый", "небесно-голубой", "оливковый", "коричневый", "бордо", "серый", "каштановый", "бежевый"]



STY=[["классический", "юбка миди", "прямые брюки", "пиджак по фигуре", "жакет по фигуре", "строгий жилет", "прямые шорты миди", "пальто приталенное"], 
["романтический", "брюки клеш", "кофта, топ с открытыми плечами", "кружевная блузка", "кружевное платье", "блузка с цветочным принтом", "платье с цветочным принтом", "пальто халат"],
["спортивный", "футболка", "спортивные штаны", "джоггеры", "кофта свободного кроя", "шорты свободного кроя"],

["повседневный", "платье шерстяное", "жакет удлиненный", "прямые джинсы", "брюки свободного кроя", "свитер оверсайз" "рубашка"]]
STYLES=defaultdict(list)
for items in STY:
    STYLES[items[0]].append(items[1:])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kek'



class MyForm(FlaskForm):
    colour = StringField('Цвет предмета одежды', validators=[InputRequired()])
    style=RadioField('Стиль',
                       choices=['классический', 'романтический', 'спортивный', "повседневный"],
                       validators=[InputRequired()])
    submit = SubmitField('Предложить наряд')


@app.route('/', methods=['GET', 'POST'])
def display():
    form = MyForm()
    result_colours=None
    result_style=None
    if form.validate_on_submit():
        if form.colour.data in COLORS.keys():
           result_colours=COLORS[form.colour.data]
        else:
            result_colours="Все оттенки черного и белого - цвета-универсалы."

        result_style=STYLES[form.style.data]


    return render_template('index.html', form=form, result_colours=result_colours, result_style=result_style)


