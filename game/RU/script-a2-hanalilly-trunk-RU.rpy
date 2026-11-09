label ru_HLT3:
    # > Random crazy idea: Any chance some of these "My my" could become "Oh my"? Some variety couldn't hurt. --Kagami
    
    #Due to rearranging callout scenes from the imachine file, this act is now playable if you select Emi's act two and skip the first scene.
    
    stop music fadeout 1.0
    
    show white
    with locationchange
    

    #show movie

    #play movie "video/note.mpg"
    
    
    centered "{font=playtime_cyr2.ttf}Примечание редактора{/font}" with dissolve
    
    nvl show dissolve
    
    n "Добро пожаловать на объединённый рут Ханако и Лилли!"
    
    n "Этот рут должен был стать особым Вторым Актом, ответвляющимся в совместный рут Ханако и Лилли."
    
    n "Изначально для открытия этого рута требовалось дойти до определённой сцены в Акте 1 со скрытым выбором, который так и не был реализован."
    
    n "Однако в конечном счёте от этой идеи отказались, и сцены так и не были закончены."
    
    n "Вплоть до сегодняшнего дня."
    
    nvl hide dissolve

    nvl clear

    window show
    
    play music music_daily 
   
    scene bg school_gardens2
    with locationchange
        
    "Смущённый, я выхожу в дверь, ведущую в сквер."

    "Шум, доносящийся с фестиваля, стал ощутимо громче."

    "Полагаю, большая часть посетителей приходит сюда во второй половине дня."
    
    "Я на секунду останавливаюсь; единственное, что я планировал на сегодня, – посмотреть выступление Лилли."

    "Теперь, когда эта задача благополучно выполнена, я не знаю, чем бы заняться."

    "К счастью, моё тело настроено более решительно, нежели я сам, и мой желудок издаёт голодное урчание в предвкушении ланча."

    scene bg school_courtyard
    with locationchange
    
    show crowd
    play sound "sfx/crowd_outdoors.ogg"
    
    "Я обхожу главное здание по асфальтированной дорожке и направляюсь туда, где сейчас разворачиваются основные мероприятия."

    "Мне требуется меньше пяти минут на то, чтобы найти палатку с лапшой, в которой заправляют трудолюбивые второклассники."

    "Мгновением спустя я становлюсь гордым обладателем тарелки недоваренной лапши."

    "Пока я с недовольной миной взираю на свою добычу, замечаю в толпе %(name_shizune)s."

    show shizu cross_angry at twoleft
    show misha hips_grin at tworight
    with charaenter

    "Идущая следом Миша как всегда глупо улыбается и, словно пьяная, размахивает из стороны в сторону розовой сахарной ватой."

    "Я пытаюсь окрикнуть их, но мой рот забит едой."

    hi "Фытфунэ! Мыфа!"

    "Конечно, %(name_shizune)s меня вряд ли услышит, но вот Миша – вполне."

    "Надеюсь, она владеет навыком «перевод говорящего с набитым ртом человека»."

    "На мгновение она замирает, но потом анимешным жестом тянет левую щёку вниз и показывает мне язык."

    "После чего догоняет подругу и они скрываются в толпе."
    
    play sound "sfx/crowd_outdoors.ogg"

    hide misha
    hide shizu
    with charaexit

    "Какой же она ещё ребёнок…"

    "Что ж, другого я и не ожидал; прошлая неделя показала мне, сколько работы легло на плечи Совета, так что побыть в таком приподнятом настроении – для неё какой-никакой отдых."

    "Ладно, мне есть ещё чем заняться."

    "…"

    "Кому я лгу?"
    
    play sound "sfx/crowd_outdoors.ogg"
    
    "Я апатично слоняюсь от киоска к киоску и никак не могу настроиться на беззаботную волну фестиваля."
    
    "Все эти палатки просто скучны на фоне выступления Лилли."
    
    "Я избавляюсь от грязной тарелки и возвращаюсь в свою комнату в общежитии."
    
    "Быть может, мне удастся отвлечься за чтением какого-нибудь ранобэ или типа того."
    
    "Нужно что-то праздничное, чтобы поднять себе настроение…"
    
    stop sound
    
    #I'm still not sure about BG cues and such, so I'll just put mine in comments
    
    #scene bg dormroom
    #with fade
    
    hide crowd
    
    scene bg school_dormhisao_ss
    with shorttimeskip
    
    stop music fadeout 0.5
    
    "Не успеваю я оглянуться, как солнце уже скрылось, освещая лишь верхушки деревьев."
    
    "Семь тридцать. Поздно же здесь темнеет."
    
    "Мне нужно более внимательно следить за временем."
    
    "Что ж, по крайней мере я приду чуть раньше."
    
    "Я возвращаю книгу на полку и иду к женскому общежитию."

    scene bg school_girlsdormhall
    with locationskip
    
    play sound "sfx/doorknock2.ogg"
    
    "Я осторожно стучу в дверь с надписью «G04», и, если честно, моё сердце бешено колотится."
    
    "Такие вот приглашения дорогого стоят."

    li "Секундочку…"

    "Из-за двери раздаётся нежный голос Лилли, в нём слышны игривые нотки. И сразу после этого я слышу едва различимый шёпот:"

    ha "Это… Хисао?"

    li "Разумеется, Ханако. Похоже, наш гость прибыл."

    "Щёлкает замок, и дверь приоткрывается."
    
    play sound "sfx/dooropen.ogg"
    
    show lilly basic_smile_paj
    with charaenter

    "За дверью стоит Лилли, она встречает меня изящным реверансом."

    li "Входи, пожалуйста, Хисао."

    #it would be now that you see the sprites.
    
    play music "bgm/To_Become_One.ogg"
    
    scene bg school_dormlilly
    with locationchange

    #it would be now that you see the sprites.
    
    #Or, you know, CG. Whatever.

    "Лилли распахивает дверь, открывая взору роскошно украшенную комнату."

    "Создаётся впечатление, что цвет дня сегодня – бледно-бежевый."

    "Всё – от тончайших на вид штор и до шёлкового покрывала на кровати – выполнено в оттенках от тёмно-коричневого и бордового до белого."
    # > I swear there should be some commas in here.  --Kagami

    "Всё, кроме двух фигур передо мной."
    
    scene ev lilly_bedroom
    with whiteout

    "Рядом со мной, всё ещё держась за дверь, стоит Лилли в тёмно-синей, почти чёрной пижаме и штанах с белой каймой."

    "Позади неё, возле низкого столика, сидит на коленях Ханако, одетая в светло-розовую ночную рубашку."

    "Руки Ханако зажаты между колен, плечи выдаются вперёд, голова опущена, будто она пытается в ней спрятаться."

    "При желании сделать это ей будет вовсе не сложно: пижама явно на пару размеров ей великовата."

    "Складки ткани делают её похожей на ребёнка, надевшего одежду родителей."

    "Она поднимает взгляд, чтобы удостовериться, что это я. На её лице проскальзывает едва заметная улыбка."

    "Я перевожу взгляд на Лилли."

    "На ней тёмная свободная пижама, явно из какого-то качественного материала. Из шёлка, я полагаю."

    "Ниже блузки с короткими рукавами – шёлковые шорты…"

    "…которые открывают взору её обнажённые очаровательно-бледные ноги…"

    "…её тонкие изящные бёдра…"

    "…гладенькие колени…"

    "…прелестные лодыжки, босые ступни…"
    
    li "Э, Хисао?"

    "Её голос вырывает меня из плена созерцания её ног."

    "Я краснею. Видимо, я сделал что-то неуместное. Даже Ханако замечает, как я пялюсь."

    "…Но я ни капли не сожалею об этом. Ни капельки."

    hi "А, не, н–ничего… Вы обе так здорово выглядите, правда-правда."

    "Я самый счастливый человек на свете."

    li "Ну, не стой в дверях. Проходи, садись."
    
    scene bg school_dormlilly
    with locationchange
    
    show hanagown normal at tworightsit
    with charaenter

    "Я вхожу в комнату, и Лилли закрывает за мной дверь."

    "Когда она поворачивается, то натыкается на меня и хватает меня за руку."
    
    show lilly basic_ara_paj at twoleft
    with charaenter

    li "Боже, боюсь, что эта комната слишком тесна для нас троих."

    "Она говорит это так, будто это что-то плохое."

    li "Проводишь меня до моего места?"

    "Немного ошарашенный, я веду Лилли к столу, на котором расставлен небольшой чайный сервиз."
    
    show lilly basic_smile_paj at twoleftsit
    with charamove

    li "Что ж, как насчёт чая? Ханако, могу я попросить тебя налить?"

    ha "Ко… Конечно. Хи… Хисао, ты…"
    
    show hanagown distant at tworightsit
    with charachange

    ha "…ты хо…"
    
    show hanagown distant_blush at tworightsit
    with charachange

    ha "…хочешь…"

    hi "Да, я не отказался бы от чашечки чая. Тебе помочь?"
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Нет… Я в порядке…"
    
    show hanagown smile at tworightsit
    with charachange

    ha "Спасибо…"
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "Ханако, всё хорошо?"
    
    show hanagown distant at tworightsit
    with charachange

    ha "Н… Нет… Я просто… Просто…"

    hi "Был тяжёлый день?"
    
    show hanagown smile at tworightsit
    with charachange

    ha "А… Ага."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange

    "Несмотря на то что я привык видеть её зажатой, сейчас Ханако улыбается, продолжая разливать чай по чашкам."

    "Я сажусь на своё место, спиной к двери."

    "По левую руку от меня сидит одетая в тёмное Лилли, по правую – розовая Ханако."

    "Чайный сервиз на столе выглядит изысканно; как если бы сама красота превратилась в фарфор цвета слоновой кости."

    "Он очень соответствует кому-то столь утончённому, как Лилли."

    "Раздаётся мелодичное «дзынь», когда Ханако, смутившись моего внимания, случайно задевает чашку носиком заварочного чайника."
    
    show hanagown worry at tworightsit
    show lilly basic_displeased_paj at twoleftsit
    with charachange

    "Она резко выдыхает; полагаю, набор столь же красив, сколь и хрупок."

    "Подходящая метафора для пары девушек, украшающих моё бытие."
    
    show hanagown worry_blush at tworightsit
    with charachange

    "Из-за своей оплошности Ханако начинает дрожать, но Лилли мягко берёт её за запястье."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Ханако, ты в порядке?"

    # Some lines snipped - Suriko

    "Ханако вскидывает взгляд на Лилли, и в нём явно читается беспокойство."

    "Думаю, Ханако не всегда такая пугливая, и, кажется, я знаю, почему она сейчас такая взвинченная."
    
    "Я нервничаю как чёрт и даже не пытаюсь это скрыть."
    
    show hanagown normal at tworightsit
    with charachange

    "Тем не менее слова Лилли, похоже, оказывают на неё благотворное влияние, и она ловко разливает чай в две оставшиеся чашки."
    
    show hanagown normal_blush at tworightsit
    with charachange

    ha "Вот, пожалуйста, Хисао… Лилли…"

    "Ханако аккуратно ставит одну чашку с блюдцем передо мной, другую – перед Лилли. Как бы мне не привыкнуть к такому обслуживанию."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Спасибо, Ханако."

    hi "А, да, спасибо, Ханако."

    ha "Пожалуйста."

    "Лилли нащупывает свою чашку и, найдя её, делает маленький глоток."
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown normal_blush at tworightsit
    with charachange

    li "Боже, как же вкусно, Ханако."
    
    ha "Спасибо."
    
    stop music fadeout 1.0
    
    #SFX Single firework
    
    play sound "sfx/fireworks.ogg"
    
    "Когда я отпиваю из своей чашки, комнату сотрясает раскат грома; я едва не проливаю кипяток на себя."
    
    stop sound 
    
    hi "Что за—?!"
    
    show lilly basic_smile_paj at twoleftsit
    with charachange
    
    li "Ох, думаю, это фейерверки."
    
    li "Самые большие, какие только бывают в этом городе."
    
    hi "Странно, никогда не слышал об этом."
    
    #sfx fireworks
    
    play sound "sfx/fireworks.ogg"
    
    play music music_dreamy 
    
    "Низкий грохот за окном всё нарастает, в то время как окрестности озаряются вспышками света."
    
    "Судя по интенсивности разрывов и свиста взмывающих в небо ракет, это не какой-то рядовой школьный фейерверк."
    
    "Хотя не думаю, что моя нынешняя компания могла бы в полной мере оценить и насладиться этим фейерверком."

    #"That would explain why both of them are here."
    
    #Is that too vauge? Lilly being blind and Hanako being burnt? Do I need to spell it out?
    # > It *would* sound good, but the fire fear isn't exactly obvious to Hisao/the player yet. Plus, the fireworks-->fire connection is reaching a bit.
    # > Nevertheless, went with an edited version of it. Commented out the last line, though; it drives home an already obvious point. --Kagami

    "Лилли немного повышает голос, чтобы быть услышанной на фоне стоящего шума."
    
    play sound "sfx/fireworks.ogg"
    
    show lilly basic_satisfied_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange

    li "Хисао, а что ты думаешь о фестивале?"

    hi "Ну… Он был намного более масштабным, чем я ожидал. Я привык к школьным фестивалям, где нет никого, кроме самих учащихся и их родителей."

    ha "Потому что этот – один из самых больших фестивалей в городе."
    
    show hanagown distant at tworightsit
    with charachange

    ha "В основном из-за фейерверков."
    
    play sound "sfx/fireworks.ogg"

    hi "Что ж, приятно видеть, как каждый напряжённо работает ради хорошего шоу."

    hi "В моей старой школе мы просто организовывали эти дурацкие кафе."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charachange

    li "Какая досада. Всё же есть определённое наслаждение от качественно проделанной работы."

    hi "Поэтому-то ты и играешь на виолончели, да?"
    
    show lilly basic_sad_paj at twoleftsit
    with charachange
    show lilly basic_smile_paj at twoleftsit
    with charachange

    "По лицу Лилли пробегает тень, но тут же без следа исчезает."

    #Fireworks SFX out
    
    li "Отчасти. Хотя порой просто не хочется, чтобы твои старания пропадали впустую."

    "Что-то подсказывает мне, что она что-то недоговаривает. Думаю, стоит сменить тему."

    hi "А… как провели сегодняшний день вы?"

    ha "Мы ходили на крышу."

    hi "На крышу?"

    #ha "The roof is on fire."

    # > I'm sorry, I had to do that. --Kagami

    # Ufufu sprite
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "Ох, Ханако имела в виду крышу главного здания."

    li "Она любит ходить туда посмотреть на толпу."
    
    show hanagown irritated at tworightsit
    with charachange

    ha "Лилли!"
    
    show lilly basic_ara_paj at twoleftsit
    with charachange

    li "Боже, я не хотела тебя задеть, Ханако. Может, лучше об этом рассказать тебе?"

    #Hanako Embarrassed
    
    show hanagown normal_blush
    with charachange

    ha "Это просто хобби."
    
    #hi "Oh, you mean the place where I met you, with the crappy fence?"
    
    hi "О, ты имеешь в виду то место, где мы встретились, со страшненьким забором?"
    ha "Д–да. Красивый вид."
    
    #SFX Pipirupirupiru pi piru pi! (Aka Lilly's phone ring)
    
    show lilly basic_surprised_paj at twoleftsit
    with charachange
    
    play sound "sfx/cellphone.ogg"

    "Ханако прерывает внезапно раздавшийся звонок телефона Лилли."
    
    li "Ах, простите."
    
    li "Вы же подождёте, пока я?.."
    
    # > I'm suddenly wondering if the way I reworded this takes away from Lilly's intent to hook them up.  --Kagami
    
    "Лилли отвечает на звонок и, нащупывая вокруг меня дорогу, выходит в коридор."
    
    hide lilly 
    with charaexit
    
    "Мы с Ханако сидим в наступившей тишине с чашками в руках."
    
    hi "А ты правда так любишь смотреть на толпу?"
    
    show hanagown worry at tworightsit
    with vpunch
    
    "Ханако чуть не давится чаем, но всё же сдерживается."
    
    #Hanako Panicked
    
    ha "Чт… Я… Не, я только… я…"
    
    show hanagown distant_alt at tworightsit
    with charachange
    
    "Кажется, что ещё немного и Ханако взорвётся; она закрывает глаза и делает глубокий вдох."
    
    show hanagown normal at tworightsit
    with charachange
    
    ha "Там хорошо. Ты можешь побыть один."
    
    hi "Отличное место, чтобы от всех скрыться, да?"
    
    ha "Т–типа того…"
    
    hi "Знал бы я раньше…"
    
    hi "Я мог бы прятаться там от %(name_shizune)s…"
    
    show hanagown smile at tworightsit
    with charachange
    
    #Hanako laugh
    
    "Ханако едва слышно хихикает, привычно пряча лицо."
    
    "Этот её тихий искренний смех, робкий и по-своему милый."
    
    "Я не могу не улыбнуться ей в ответ."
    
    ha "Похоже, они заставляли тебя вкалывать всю прошедшую неделю…"
    
    hi "Ты права. Никогда ещё меня так не припахивали в школе."
    
    show lilly basic_weaksmile_paj at twoleftsit
    with charaenter
    
    show hanagown normal at tworightsit
    with charachange
    
    "Возвращается Лилли, и я помогаю ей пройти на место."
    
    li "Прошу прощения – важный звонок."
    
    hi "Ох, что-то связанное со школой?"
    
    show lilly basic_listen_paj at twoleftsit
    with charachange
    
    li "Нет, это был мой репетитор по виолончели."
    
    li "Она отменила следующее занятие."
    
    "Я немного удивляюсь тому, что Лилли берёт уроки."
    
    "С другой стороны, есть же у спортсменов тренер. Век живи – век учись, как говорится."
    
    show lilly basic_smileclosed_paj at twoleftsit
    with charachange
    
    li "Как бы то ни было, а в следующие выходные я совершенно свободна."
    
    li "Хисао, не составишь нам с Ханако компанию?"
    
    li "Это хороший шанс познакомиться с городом."
    
    hi "Звучит неплохо. А что, есть какие-то предложения?"
    
    show hanagown smile_blush at tworightsit
    with charachange
    
    "Глаза Ханако вспыхивают из-под чёлки."
    
    ha "Мы… Мы могли бы сходить на пикник…"
    
    show lilly basic_satisfied_paj at twoleftsit
    with charachange
    
    li "Замечательная идея. Как думаешь, Хисао?"
    
    hi "Я не смог бы придумать ничего лучше."
    
    show lilly basic_ara_paj at twoleftsit
    show hanagown smile at tworightsit
    with charachange
    
    li "Хорошо, решили."
    
    li "Мы с Ханако приготовим что-нибудь перекусить, так что можешь об этом не переживать."
    
    hi "Замечательно. Мне эта идея нравится всё больше и больше…"
    
    stop music fadeout 5.0
    
    "Я завершаю предложение длительным зевком."
    
    hi "О, прошу прощения…"
    
    show lilly basic_weaksmile_paj at twoleftsit
    show hanagown normal at tworightsit
    with charachange
    
    li "Ничего страшного. Однако, полагаю, нам стоит уже расходиться."

    hi "Думаю, просто я немного устал за эту неделю."

    ha "Да уж, все мы немного устали…"

    hi "Ага… Ну, я пойду."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    li "Спасибо за этот вечерний визит, Хисао."
    
    #"Thank you for your presence"? Was that intentional wording on her part, or...? 

    hi "Спасибо за приглашение… и на сегодня, и на следующие выходные, да."
    
    hi "Но сейчас я всё-таки, пожалуй, пойду."
    
    show hanagown normal_blush at tworight
    with charamove
    
    "Я встаю и направляюсь к двери; Ханако осторожно встаёт позади меня и идёт следом."

    "Немного озадаченный, я поворачиваюсь к ней."

    hi "Ты уходишь вместо со мной?"
    
    play music "bgm/Generic_Happy.ogg"
    
    show hanagown worry_blush at tworight
    with charamove

    "Ханако мгновенно заливается румянцем."

    ha "Нет! Я… Не… Эта комната… Не…"

    # Ufufu sprite
    
    show lilly basic_giggle_paj at twoleftsit
    with charachange

    li "Боже, Хисао, какая дерзость…"

    hi "Да ладно, шучу."
    
    show lilly basic_smile_paj at twoleftsit
    with charachange

    "Но я, кажется, всё-таки смутил её."

    "Мне неловко, но её лицо в такие моменты просто очаровательно."
    
    "Она закрывает руками обожжённую часть лица и смотрит на меня поверх ладоней."
    
    show hanagown distant at tworight
    with charachange
    
    "Но, как только она ловит мой взгляд, тут же отводит глаза в сторону."
    
    "Она такой ребёнок…"

    ha "А… Да… Спокойной…"

    li "Спокойной ночи, Ханако, Хисао."

    hi "Спокойной ночи."

    "На этом наше чаепитие и заканчивается."

    scene bg school_girlsdormhall
    with locationchange

    "Когда мы с Ханако выходим из комнаты, Лилли закрывает за нами дверь."
    
    play sound "sfx/doorclose.ogg"

    "Ханако скрывается за дверью, и я вижу табличку с её именем."

    "Думаю, это многое объясняет."

    "Я направляюсь обратно в общежитие, и это высасывает из меня остатки энергии."
    
    stop music fadeout 1.0
    
    scene bg school_dormhisao_ni
    with shorttimeskip

    "Стоит мне войти в комнату, как чувствую полное измождение; события сегодняшнего дня берут своё."

    "Я скидываю ботинки и падаю на кровать, засыпая раньше, чем голова касается подушки."

    scene black
    with dissolve

    return

label ru_HLT4:

    #Yeah, since this is a pretty big change I'm just going to repost it.
    #I think I've got all the calls/tags right, but it's probably worth checking them

    #Also, there is a 6-day gap between the last scene and this one. I've done this for 2
    #reasons.
    #First, it allows us to put in an interstitial if we need it, or we can put one of the
    #"common" scenes here.
    
    # > What's that second reason? --Kagami

    #Scene starts as a fade from dark
    #We have BGs to match this now, so this is no longer a need
    
    scene bg school_dormext_full
    with None
    
    play music music_soothing 

    "Стоя перед женским общежитием, я осознаю, что это первый выходной с момента моего появления в «Ямаку»."

    "И, по сравнению с беспокойной предфестивальной неделей, обычные школьные занятия проходят относительно спокойно."

    "После уроков бывает так скучно, что я регулярно ловлю себя на том, что листаю немногочисленные привезённые с собой книги."

    "Но спасение уже близко."

    "Я никому не признаюсь, но я жутко жду этого пикника в конце недели."

    "В смысле, какой парень будет ждать какого-то там пикника?"

    "Дверь общежития со скрипом открывается, и передо мной появляются Ханако и Лилли."

    #Maintaining the outfits from the SVN scene, but they can change.
    
    show lilly cane_smileclosed_cas at twoleft
    show hanako emb_timid_sun at tworight
    with charaenter

    "На Лилли надета юбка до колен и светлая, явно дорогая, рубашка."

    "Несмотря на то что технически её одежда менее откровенна, чем школьная форма, вырез на рубашке и длина юбки выглядят очень соблазнительно."

    "Ханако одета в длинное бледно-жёлтое платье."

    "Как и школьная форма, платье явно ей на пару размеров великовато."

    "Перед собой в руках она держит небольшую корзинку для пикника, тем самым словно отгораживаясь от окружающего мира."

    hi "Доброе утро, Лилли, Ханако."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "Ох, ты уже тут, Хисао? Как ты?"

    hi "Лучше всех. А вы как, ребят?"

    li "Я как никогда бодра и с нетерпением жду, когда мы отправимся."

    hi "Приятно слышать. А ты, Ханако?"
    
    show hanako emb_shock_sun at tworight
    with charachange

    "Когда я поворачиваюсь к ней, Ханако подскакивает и прижимает корзинку к груди."

    #Hanako looking down/away
    
    show hanako emb_downtimid_sun at tworight
    with charachange

    ha "Э… Хоро… Спаси… бо."

    hi "Что ж, не пора ли нам отправляться?"

    li "Ах да, пожалуй."

    hi "У меня только один вопрос: куда именно мы идём?"
    
    show lilly cane_planned_cas at twoleft
    with charachange

    li "Есть тут небольшой парк неподалёку. Поскольку он расположен несколько в стороне от жилых районов, людей там, как правило, немного."

    hi "Отлично. Как нам туда добраться?"

    li "Пешком, тут недалеко."

    #Bg change to empty street w/ fade
    
    scene bg school_road
    with shorttimeskip
    
    show lilly cane_listen_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charaenter

    "­Это «недалеко» на деле больше напоминает поход."

    "У меня на лбу выступили капельки пота, пока мы проходим улицу за улицей."

    hi "Сколько же нам ещё идти?"
    
    show lilly cane_surprised_cas at twoleft
    with charachange

    li "Я не уверена. На какой мы улице?"

    "Я оглядываюсь вокруг в поисках указателя с названием улицы."
    
    show hanako emb_timid_sun at tworight
    with charachange

    ha "Улица Хиробы."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "А, значит, не так уж и далеко. Ещё квартал или два."

    "Мы продолжаем свой путь, выстроившись в ряд, с Лилли во главе."
    
    stop music fadeout 1.0
    
    show hanako emb_downsad_sun at tworight
    with charachange

    "Неожиданно Ханако сбивается с ноги и пристраивается за спиной Лилли, прижав корзинку к груди и низко опустив голову."

    hi "Ханако? Что случилось?"

    #hanako cowed
    
    play music music_hanako

    ha "Тс-с, они смотрят на меня."
    
    show lilly cane_displeased_cas at twoleft
    with charachange

    hi "Кто?"

    "Ханако не отвечает и лишь молча кивает вперёд."

    "Там я вижу идущих нам навстречу мужчину и женщину, разговаривающих друг с другом."

    "В этот момент они замечают нашу троицу."

    "Пару секунд они смотрят на нас, но, заметив трость Лилли, отводят взгляд."

    hi "Ханако, они не смотрят на тебя."

    hi "Видишь?"
    
    show hanako emb_sad_sun at tworight
    with charachange

    "Ханако немного поднимает голову, мягко качнув чёлкой."

    "Под ней я замечаю глаза, ищущие подтверждения моим словам."

    #once again, if I lose the "disability" debate, we can throw in a line here about "OMG
    #BURNS"
    
    show hanako emb_downsad_sun at tworight
    with charachange

    "Она замечает эту пару и снова опускает голову."

    ha "Смотрят. Точно."

    hi "Да нет же, по…"

    "Я снова бросаю взгляд на пару. Они словно изо всех сил стараются не обращать на нас внимания."
    
    "До меня вдруг доходит, что имела в виду Ханако."
    
    show lilly cane_sad_cas at twoleft
    with charachange

    "Даже если забыть про нашу форму очевидно, что мы из «Ямаку»."

    "Помимо школы, в этой части города очень мало домов, и трость Лилли выдаёт нас с головой."

    "Однако, из-за того, что эти люди так старательно избегают на нас смотреть, чувство такое же, как если бы они сверлили нас взглядами."

    "Полагаю, Ханако частенько становится центром такого рода внимания."

    "Даже несмотря на все её старания и мешковатую одежду, некоторые шрамы на руках и лице всё ещё отлично заметны."

    "Это, должно быть, тяжело – осознавать, что, несмотря на все усилия, люди продолжают на тебя пялиться."

    "Я иду бок о бок с Ханако, встав между ней и этими людьми."

    hi "Теперь точно всё."
    
    stop music fadeout 5.0

    ha "Спа… сибо…"
    
    show lilly cane_weaksmile_cas at twoleft
    show hanako emb_downtimid_sun at tworight
    with charachange

    "Ханако так и идёт вслед за Лилли с низко опущенной головой, всё ещё боясь поднять взгляд."

    "Я оставляю её, догоняю Лилли и пристраиваюсь с ней рядом."

    li "Ах, вот ты где."
    
    show lilly cane_smile_cas at twoleft
    with charachange

    li "Я уже начинаю думать, что не лучшим образом подхожу на роль поводыря."

    hi "А?"

    hi "Ой, прости!"

    "Я отвлёкся на Ханако и совсем забыл, что Лилли нужен кто-то, кто мог бы читать для неё названия улиц."

    li "Насколько я помню, следующая улица направо – это проспект Касанеру, да?"

    hi "Эм… Ну, похоже на то."

    li "Хорошо. Это пункт нашего назначения."
    
    show lilly cane_smileclosed_cas at twoleft
    with charachange

    "Парк совершенно пуст, как Лилли и предсказывала."

    #scene change to datin' park.
    
    scene bg suburb_park
    with locationchange
    
    play music "bgm/Daylight.ogg"

    "Он представляет собой засаженный травой участок между двумя перекрёстками."

    "С одной стороны имеется небольшая рощица, но кроме неё больше ничего нет, только трава."

    "Мы входим под сень деревьев, и я беру у Ханако корзину."
    
    show lilly cane_smile_cas at twoleft
    show hanako emb_downtimid_sun at tworight
    with charaenter

    hi "Здесь. Позволь мне помочь."

    "Ханако неохотно, но отдаёт мне корзинку."
    
    show hanako emb_timid_sun at tworight 
    with charachange

    "И сразу же отбегает к Лилли. Возможно, она всё ещё не отошла от недавнего инцидента."
    
    show hanako emb_timid_sun at left
    with charamove
    
    show lilly cane_weaksmile_cas at twoleft
    with charachange

    "Я открываю корзину и извлекаю из неё полосатый плед, который и раскладываю в тенёчке."

    hi "Не хотите присесть, пока я тут всё распакую?"

    li "Пожалуй. Прогулка длилась несколько больше, чем я ожидала."

    "Ханако кивает и подводит Лилли к одеялу."

    "Убедившись, что с Лилли всё в порядке, Ханако садится между нами."
    
    show lilly basic_smileclosed_cas at twoleftsit
    with charamove
    
    show hanako emb_timid_sun at tworight
    with charachange
    
    show hanako emb_timid_sun at tworightsit
    with charamove

    ha "Д-давай я… помогу…"

    "Ханако ныряет в корзину и начинает доставать различные пакетики с закусками, раскладывая их перед нами."

    "Я заглядываю внутрь и на дне корзины замечаю термос."

    hi "О, у нас есть что попить? А то в горле пересохло…"

    li "Ах, конечно. Ханако, не могла бы ты достать?"
    
    show lilly basic_smile_cas at twoleftsit
    with charachange

    ha "К–конечно…"

    "Она достаёт из корзины металлический цилиндр и протягивает его мне, следом на свет появляются три чашки."
    
    show hanako emb_downsmile_sun
    with charachange

    hi "Всем наливать?"

    li "Если не затруднит, пожалуйста."

    "Я наполняю чашки тёмной прохладной жидкостью."

    "Каждый берёт себе по чашке, и мы начинаем чаепитие."

    "Чай со льдом – это здорово."

    #I've softened the original "drinking" session, however since it's a recurring theme
    #I think that it should be kept in. Unless, of course, we drop all drinking.
    #But that's a little unrealistic.
    
    #Well, due to popular demand, drinking is now kaput.
    # > The Itis does not work here at all. Maybe play up the sunny weather angle? --Kagami

    "Некоторое время мы молчим; думаю, от каждого из нас прогулка потребовала немало сил."

    li "Ну как, Хисао, тебе нравится?"

    hi "Да, неплохо. Что это? Я хотел бы купить немного на обратной дороге."
    
    li "Это будет проблематично, так как я сделала его сама."
    
    #Lilly ufufuf maybe?
    
    show lilly basic_planned_cas at twoleftsit
    with charachange
    
    hi "Серьёзно? Вот уж не ожидал…"
    
    li "Ох, тебе скучно?"

    #Lilly concerned
    
    show lilly basic_concerned_cas at twoleftsit
    with charachange

    hi "Нет, вовсе нет. Просто… очень много неожиданностей."

    ha "Эм… Готово…"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    "Ханако прерывает нашу беседу и переключает внимание на еду перед нами."

    hi "Ого, сколько тут всего… Как только это в корзину-то влезло?"

    ha "Опыт… наверное…"

    hi "Выглядит аппетитно, да и я проголодался. Где ты всё это купила?"

    ha "Ну, эм…"

    #Hanako embarrassed
    
    show hanako emb_emb_sun at tworightsit
    with charachange

    li "Ханако почти всё это приготовила ночью, зная, что мы пойдём на пикник."
    
    show lilly basic_satisfied_cas at twoleftsit
    with charachange

    hi "Ты всё это сделала сама?"

    ha "Как-то так… Наверное…"
    
    show hanako emb_smile_sun at tworightsit
    with charachange

    hi "Что ж, не позволим еде пропасть."

    #Fuck sake she's being Nerine. I HATE Nerine
    # > Who? --Kagami
    #Character from "Shuffle!". Basically a walking doormat, she's passive and modest and that basic nice girl shit

    "Мы начинаем трапезу, и вскоре перед нами остаётся один только целлофан."
    
    with shorttimeskip
    hide hanako
    
    stop music fadeout 2.0
    
    "Я снова наливаю всем чай из термоса и замечаю, что он практически пуст."
    
    # > You must build additional food descriptions. --Kagami

    "Из-за сочетания еды, полуденного солнца и долгой прогулки на меня нападает сонливость."

    "…И, похоже, не на меня одного."
    
    show lilly basic_sleepy_cas at twoleftsit
    with charachange
    
    "Ханако, кажется, уже задремала, склонив голову на колени Лилли." #- too bad we don't have sleepy-like sprites for Hanako in her dress, ksdevs. she'll go spriteless
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Лилли принимает свою чашку из моих рук и манит меня пальцем."
    
    show lilly basic_weaksmile_cas_close at twoleftsit
    with charachange

    "Я наклоняюсь к ней, и она шепчет:"

    li "Она уснула?"

    "Я бросаю взгляд на Ханако, которая кажется мирно дремлющей."

    hi "Похоже на то."

    li "Тогда могу я попросить тебя об одолжении?"

    hi "Конечно."

    li "Ты не мог бы снять её с меня?"

    "Мне требуется пара секунд, чтобы осознать суть её просьбы."

    "Ханако практически лежит на Лилли; наверняка ей неудобно."

    hi "Без проблем."

    "Я аккуратно беру Ханако за плечи и укладываю на плед."
    
    show lilly basic_listen_cas at twoleftsit
    with charachange

    "Лилли расправляет плечи, осторожно их разминая."

    li "Спасибо. Я не хотела её будить."

    hi "Всё в порядке. Может, оставим её тут ненадолго, а сами прогуляемся?"

    hi "А то чего мы перешёптываемся тут…"
    
    show lilly basic_smile_cas at twoleftsit
    with charachange

    li "Хорошая мысль. Можешь помочь мне встать?"

    "Лилли протягивает обе руки вперёд в международном сигнале «Помоги мне встать»."

    #cut the next two lines if you wish. Just moar Lilly fanservice
    
    show lilly basic_smile_cas at twoleft
    with charamove

    "Я помогаю, в том числе ещё и потому, что после этого в воротничке её рубашки образовался заманчивый вырез, открывая отличный… обзор."

    "Чёрт, майка… Ладно, попытка не пытка."
    
    show lilly basic_smile_cas at centersit
    with charamove

    "Мы отходим к ближайшему дереву и садимся спиной к стволу."
    
    # > Tree scene could maybe use a bit more detail in its setup. Just another line or two, maybe three?  --Kagami

    "Здесь мы можем следить за Ханако, не боясь потревожить её сон."

    #I'm cutting this here for two reasons. Firstly, H5r will have a lot of the stuff from H6,
    #and also Miku just arrived, and it would be rude of me not to play with her.

    #I'd like to say I'm looking for feedback, but I'm really not.
    # > YOU GONNA GET FEEDBACK'D
    
    # > ....well, actually, you already have been. --Kagami

    return



label ru_HLT5:
    
    play music music_soothing 

    hi "И часто вы вот так куда-либо выбираетесь?"
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "Ну, в какой-то степени. Я стараюсь водить её в такие места, где никто её не будет беспокоить."
    
    li "В этом смысле я рада, что ты пошёл с нами."

    hi "Я? Почему?"

    li "Как по мне, она тебе доверяет."

    hi "В это сложно поверить."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    "Она улыбается своей фирменной улыбкой, поднеся к губам согнутый палец."

    li "Ханако есть Ханако. Понять её порой бывает затруднительно."

    "Это ещё мягко сказано."
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Как бы то ни было, с тобой она чувствует себя комфортнее, чем с кем-либо ещё. Ты прекрасно ей подходишь."

    "Она очаровательно улыбается, совершенно выбивая меня из колеи."

    li "Спасибо, Хисао."

    hi "А… Ну… всегда пожалуйста… Наверное."
    
    show lilly basic_smile_cas at centersit
    with charachange

    "Ещё одна улыбка."

    "Её улыбка такая широкая и искренняя, что я никак не могу выбросить её из головы."
    
    show lilly basic_surprised_cas at centersit
    with charachange

    hi "Эм… Лилли… А как вы с Ханако подружились?"
    
    show lilly basic_reminisce_cas at centersit
    with charachange

    "Помедлив секунду, Лилли откидывается назад и задумывается."

    li "Поначалу Ханако была словно в скорлупе."

    li "Она ни с кем не разговаривала, в том числе и со мной, хоть мы и жили в соседних комнатах."

    li "Каждое утро я пыталась завязать с ней разговор, но она всегда ускользала от меня."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    hi "И… что случилось потом?"

    "Она глубоко вздыхает и в задумчивости потирает подбородок."

    li "Хм… Кажется, это произошло на третью неделю её пребывания в «Ямаку»."
    # > "a fledgling's romance"     a what? --Kagami

    li "Одну девочку из соседней комнаты бросил её молодой человек. Это были юношеские романтические отношения, но она была вся в слезах."

    li "В конечном итоге девочка эта пришла ко мне в комнату. Я была старостой класса и просто её знакомой, и она решила довериться мне."

    li "Я напоила её чаем, и, после того как она поделилась со мной своим горем, ей стало лучше."
    # > ...Wait, what?  She heard them standing?

    li "Когда она ушла, я почувствовала, что кто-то молча стоит возле моей двери."

    li "Оказывается, Ханако всё слышала сквозь стену и решила узнать, не смогу ли я помочь ей."

    li "Кажется, что это из-за того, что она осознала, что я слепая… Это её успокоило, что ли."

    li "До тех пор она до жути боялась всех и каждого."

    li "Моя слепота позволила ей расслабиться достаточно для того, чтобы открыться мне."

    li "Так мы с ней и подружились."
    
    show lilly basic_sad_cas at centersit
    with charachange

    "Она на мгновение задумывается."

    "На её лице появляется тень сожаления."

    li "К сожалению, я единственная, с кем она смогла подружиться."

    li "Я чувствую, что подвела её."

    hi "Подвела?"

    li "Я старалась сделать так, чтобы она чувствовала себя увереннее среди людей, но, несмотря на все усилия, мне так это и не удалось."

    li "Я уверена, что в глубине души она очень добрая, но она как-будто осознанно замыкается."
    
    show lilly basic_listen_cas at centersit
    with charachange

    hi "Понятно."

    "Воцаряется тишина."

    "В этот момент я осознаю, что она кое о чём умолчала."

    "Точнее, о её роли в их отношениях."
    
    show lilly basic_sleepy_cas at centersit
    with charachange

    "Она так заботится о Ханако, но что же она сама?"
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    "Прежде чем я успеваю задать ей это вопрос, Лилли зевает."

    li "Ох, прошу прощения."
    
    li "Просто меня неожиданно стало клонить в сон."

    #"I can see that Lilly is gently trying to change the topic, so I decide to leave my questioning at that."

    return



label ru_choiceHLT5:

    #Choice:
    #1 – Stay with Lilly
    #2 – check on Hanako

    menu:
        with menueffect
        
        "Я понимаю, что Лилли старается осторожно сменить тему, так что решаю оставить этот вопрос на потом."

        "{font=playtime_cyr2.ttf}Остаться с Лилли.{/font}":
            return m1
        
        "{font=playtime_cyr2.ttf}Проведать Ханако.{/font}":
            return m2



label ru_HLT5a:

    #1 – Staying with Lilly
    #+1 lilly
    
    # > I thought we weren't using points anymore. Or is that just A1F?   --Kagami
    
    stop music fadeout 1.0
    

    hi "Ты права, такие дни хороши."

    hi "Можешь делать что хочешь и когда хочешь."

    hi "В некотором смысле это освежает."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    #Lilly Ufufufu

    "Лилли устало улыбается."

    li "Знаешь, что-то подобное сказала Ханако примерно год назад."

    hi "Правда? И что же она сказала?"
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Ну, мы с ней отдыхали в моём летнем домике, и она заметила, что любит тратить время на себя."

    hi "В летнем домике?"
    
    show lilly basic_smile_cas at centersit
    with charachange

    li "Моя семья владеет небольшим летним домиком к северу отсюда. Хотя я была там всего несколько раз."

    li "Мы с Ханако ездили туда во время летних каникул последние два года."

    li "Я очень хотела бы хоть раз съездить туда зимой; говорят, там очень здорово, когда выпадает снег."

    hi "Тебе нравится снег?"
    
    show lilly basic_planned_cas at centersit
    with charachange

    li "М-м-м-м… Он прекрасен."

    "Он такой… необычный на ощупь."

    "Если честно, сложно предположить, что может быть привлекательного в снеге для той, что не может его видеть."

    hi "Чтобы иметь летний домик… это ж сколько денег нужно? В наши дни жильё ужасно дорого."
    
    show lilly basic_listen_cas at centersit
    with charachange

    li "Ах… Возможно, ты слышал о компании Tachibana Enterprises?"

    hi "Tachibana Enterprises… Что-то знакомое…"

    hi "Точно! Недавно они нашли большое месторождение алмазов в Южной Африке. Несколько дней назад это было во всех новостях."

    li "Да, это они."

    li "Мой отец – один из членов правления."
    
    play music music_night

    "У меня отвисает челюсть."

    "Один из членов правления? Компании по добыче алмазов?!"

    "Даже если они лишь изредка появляются на приисках, это объясняет, как она может позволить себе такие вещи."

    hi "Это… изумительно."
    
    show lilly basic_concerned_cas at centersit
    with charachange

    "Я поворачиваюсь к ней и осознаю, что затронул, возможно, неловкую для неё тему."

    li "Это… не так уж и круто…"

    "Видимо, понимая того, что она только что сказала, она пытается поскорее меня успокоить."

    li "Ох, извини. Это всё немного… странно. Как бы то ни было, это и есть источник моего финансового благополучия."

    hi "Ясно…"

    "Но я всё равно испытываю неудобство за свою реакцию."

    "В любом случае стоит сменить тему."
    
    # > I'm trying to figure out what he's supposed to be feeling guilty about, and I just can't.

    hi "Прости, я немного устал."

    "Я очень вовремя зеваю, как бы ставя точку в нашем разговоре."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "Вынуждена признать, что и я тоже. Может, нам вздремнуть?"

    hi "Звучит неплохо."
    
    hide lilly
    with charaexit

    "Лилли отодвигается от ствола дерева и укладывается на травке."

    #"As I follow her lead, laying in the shade of the tree as well, it doesn't take long for sleep to overcome me."

    #"Moments before I shut my heavy eyes, I can just remember one thought."

    #hi "It'd be nice to see the summerhouse."

    #li "…It would."

    #End Part 1

    "Следуя её примеру, я тоже укладываюсь в тени дерева. Сон не заставляет себя долго ждать."
    "За мгновение до того, как я закрываю глаза, я кое-что вспоминаю."
    hi "Было бы здорово побывать в этом летнем домике."
    li "…Было бы."
    return



label ru_HLT5b:

    #2 – Check on Hanako
    #+ 1 Hanako

    hi "Я собираюсь проведать Ханако."
    li "А, неплохая идея."
    li "В таком случае ты не обидишься, если я вздремну?"
    hi "Нет, конечно. Отдыхай на здоровье."

    li "Благодарю."

    #li "But in that case, would you be offended if I took a nap?"

    #hi "Not at all. Please do."

    #li "Thank you."

    #"Lilly slides down the trunk of the tree until she lays flat on the grass."

    "Лилли отодвигается от ствола дерева и укладывается на травке."

    "Бросая взгляд на спящую фигуру Ханако, я вспоминаю слова Лилли."

    "До этого момента я рассматривал её шрамы только с физической точки зрения."

    "Однако я думаю, что они ещё и психологические."

    "И после увиденного утром я запросто могу в это поверить."

    "Знать, что каждый человек будет судить о тебе только по твоему лицу, – это достаточно трудно."

    "Не знаю, смог бы я справиться с подобным давлением."

    "Мои чувства обращаются к спящей фигуре; я встаю и делаю пару неуверенных шагов по направлению к ней."

    "Большая ошибка."

    "Я слишком долго сидел в тенёчке, особенно после столь продолжительной прогулки."

    "После столь резкого подъёма у меня закружилась голова."

    "Это заставляет меня сесть обратно."
    
    stop music fadeout 2.5
    
    scene black
    with shuteye

    #End splits

    "Чтобы прийти в себя, я на секунду закрываю глаза…"
    return



label ru_HLT5x:
    
    scene bg suburb_park
    with openeye

    "Лёгкий ветерок пробуждает меня ото сна."

    "Я протираю глаза и оглядываюсь по сторонам."
    
    play music music_tranquil

    "Небо сменило глубокую синеву дня на жёлто-синий цвет раннего вечера."

    "Полагаю, все мы на некоторое время отключились."
    
    show hanako emb_downtimid_sun at tworightsit
    with charaenter

    "Лилли ещё крепко спит под деревом, тогда как Ханако, кажется, просто дремлет, сидя рядом с ней, обхватив колени."

    hi "Эй, Ханако, давно ты так сидишь?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Н… Не очень."

    ha "Я… я тоже только что проснулась."

    "Она немного ёрзает, и я замечаю у неё за спиной корзину для пикника, собранную в обратную дорогу."

    "Кто знает, как долго она уже тут сидит, ожидая нашего пробуждения, но не желая нас потревожить."

    hi "Что ж, будим Лилли?"
    
    show hanako emb_downsad_sun at tworightsit
    with charachange

    ha "Эм… Я не… Эм…"

    hi "Всё нормально. Не думаешь, что Лилли сочтёт ужасно оскорбительным спать, заставляя нас ждать её пробуждения?"

    "Ханако ненадолго задумывается."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Да… Пожалуй…"
    
    #I'm going to keep the "falling" bit 'cause I think that it's fun. And it might be moe. I don't know, obviously.
    
    show hanako emb_timid_sun at centersit
    with charamove

    "Она наклоняется вперёд с намерением разбудить Лилли…"
    
    show hanako emb_strain_sun at centersit
    with charachange

    "…запутывается в одежде…"

    "…и падает прямо на Лилли."
    
    show hanako emb_shock_sun at centersit
    show lilly basic_surprised_cas at twoleftsit
    with vpunch

    "Лилли тут же просыпается и начинает обшаривать всё вокруг руками, пытаясь понять, что происходит."
    
    show hanako emb_downsad_sun at centersit
    with charachange

    ha "Прости, Лилли! Прости, прости!"

    ha "Я просто… Немножко упала…"
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Лилли берёт себя в руки на удивление быстро, принимая во внимание внезапность пробуждения."

    li "Боже, всё в порядке, Ханако."

    li "Подобные неловкости случаются."
    
    show lilly basic_weaksmile_cas at twoleft
    with charamove

    "Лилли поднимается, держа её за руку."
    
    show hanako emb_downtimid_sun at center
    with charamove

    "Ханако берёт корзину и встаёт рядом."

    hi "Думаю, пора возвращаться, да?"

    li "Да уж, я не отказалась бы принять душ и поваляться в своей постели."
    
    show lilly basic_displeased_cas at twoleft
    with charachange

    li "Не скажу, что спать под деревом очень удобно…"

    "Посреди фразы Лилли теряет равновесие и я придерживаю её за плечо."
    
    show lilly basic_weaksmile_cas at twoleft
    with charachange

    li "Ох, спасибо, Хисао."
    
    show lilly basic_sleepy_cas at twoleft
    with charachange

    li "У меня немного закружилась голова."

    hi "Мне это знакомо."

    li "Не знаю, как ты, но я не представляю, как дойду обратно."

    hi "А как же мы тогда вернёмся в «Ямаку»?"

    #Lilly disappointed/deep thought/something like that
    
    show lilly basic_listen_cas at twoleft
    with charachange

    li "Что ж, я предложила это место, мне и ответ нести."

    "Не успеваю я возразить, как Лилли достаёт сотовый телефон и начинает кому-то звонить."

    "Пока она набирает, я отмечаю про себя, что все кнопки имеют выступы."

    "Полагаю, это объясняет, как она может так быстро набирать номер."

    li "Здравствуйте. Могу я заказать такси к парку Касанеру? Спасибо."
    
    scene bg school_road_ss
    with locationskip

    "Как ни странно, такси прибывает довольно скоро."

    "Мы втискиваемся на заднее сиденье, Ханако садится между Лилли и мной."

    li "В «Ямаку», будьте добры."

    "Водитель такси" "Будет сделано."

    "Расстояние, на которое утром у нас ушёл битый час, мы проезжаем за несколько минут; и вот мы уже стоим перед женским общежитием."
    
    scene bg school_dormext_full_ss
    with shorttimeskip

    #BG change to dorms
    
    show lilly basic_smile_cas at twoleft
    show hanako emb_smile_sun at tworight
    with charaenter

    hi "Что ж, спасибо вам обеим."

    hi "Я хорошо провёл время."

    li "Пожалуйста."

    hi "Спасибо за ланч, Ханако."

    "Прежде чем ответить, Ханако немного краснеет."
    
    show lilly basic_planned_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charachange

    #Hanako smile/blush

    ha "По… пожалуйста."

    hi "Эх, я устал. Жду не дождусь, когда смогу принять душ или типа того…"

    li "Ты совершенно прав."

    ha "Да… Я тоже…"

    hi "Ну, увидимся завтра в школе?"

    li "Буду ждать с нетерпением."

    ha "До… доброй ночи."

    hi "Доброй. Ханако, Лилли."
    
    hide hanako
    hide lilly
    with charaexit

    "Мы коротко киваем друг другу, и девушки исчезают за дверью."

    "Я с облегчением вздыхаю. Не то чтобы мы много двигались, но дневной сон под открытым небом истощил меня."

    "И потребовались неимоверные усилия, чтобы пройти короткий путь до моей комнаты и в изнеможении упасть на кровать."

    #Fade to black.

    #Next scene will probably borrow heavily from the old H7, but with a more obvious
    #pointer as to with path you take. I'll have that, and hopefully H7r done tomorrow.
    return



label ru_HLT6:
    
    stop music fadeout 1.0
    
    "Я понимаю, что Лилли старается осторожно сменить тему, так что решаю оставить этот вопрос на потом."

    hi "Ты права, такие дни хороши."

    hi "Можешь делать что хочешь и когда хочешь."

    hi "В некотором смысле это освежает."
    
    show lilly basic_giggle_cas at centersit
    with charachange

    #Lilly Ufufufu

    "Лилли устало улыбается."

    li "Знаешь, что-то подобное сказала Ханако примерно год назад."

    hi "Правда? И что же она сказала?"
    
    show lilly basic_smileclosed_cas at centersit
    with charachange

    li "Ну, мы с ней отдыхали в моём летнем домике, и она заметила, что любит тратить время на себя."

    hi "В летнем домике?"
    
    show lilly basic_smile_cas at centersit
    with charachange

    li "Моя семья владеет небольшим летним домиком к северу отсюда. Хотя я была там всего несколько раз."

    li "Мы с Ханако ездили туда во время летних каникул последние два года."

    li "Я очень хотела бы хоть раз съездить туда зимой; говорят, там очень здорово, когда выпадает снег."

    hi "Тебе нравится снег?"
    
    show lilly basic_planned_cas at centersit
    with charachange

    li "М-м-м-м… Он прекрасен."

    "Он такой… необычный на ощупь."

    "Если честно, сложно предположить, что может быть привлекательного в снеге для той, что не может его видеть."

    hi "Чтобы иметь летний домик… это ж сколько денег нужно? В наши дни жильё ужасно дорого."
    
    show lilly basic_listen_cas at centersit
    with charachange

    li "Ах… Возможно, ты слышал о компании Tachibana Enterprises?"

    hi "Tachibana Enterprises… Что-то знакомое…"

    hi "Точно! Недавно они нашли большое месторождение алмазов в Южной Африке. Несколько дней назад это было во всех новостях."

    li "Да, это они."

    li "Мой отец – один из членов правления."
    
    play music music_night

    "У меня отвисает челюсть."

    "Один из членов правления? Компании по добыче алмазов?!"

    "Даже если они лишь изредка появляются на приисках, это объясняет, как она может позволить себе такие вещи."

    hi "Это… изумительно."
    
    show lilly basic_concerned_cas at centersit
    with charachange

    "Я поворачиваюсь к ней и осознаю, что затронул, возможно, неловкую для неё тему."

    li "Это… не так уж и круто…"

    "Видимо, понимая того, что она только что сказала, она пытается поскорее меня успокоить."

    li "Ох, извини. Это всё немного… странно. Как бы то ни было, это и есть источник моего финансового благополучия."

    hi "Ясно…"

    "Но я всё равно испытываю неудобство за свою реакцию."

    "В любом случае стоит сменить тему."

    hi "Прости, я немного устал."

    "Я очень вовремя зеваю, как бы ставя точку в нашем разговоре."
    
    show lilly basic_weaksmile_cas at centersit
    with charachange

    li "Вынуждена признать, что и я тоже. Может, нам вздремнуть?"

    hi "Звучит неплохо."
    
    hide lilly
    with charaexit

    "Лилли отодвигается от ствола дерева и укладывается на травке."

    hi "Я собираюсь проведать Ханако."

    li "А, неплохая идея."
    li "В таком случае ты не обидишься, если я вздремну?"
    hi "Нет, конечно. Отдыхай на здоровье."
    li "Благодарю."
    "Лилли отодвигается от ствола дерева и укладывается на травке."

    "Бросая взгляд на спящую фигуру Ханако, я вспоминаю слова Лилли."

    "До этого момента я рассматривал её шрамы только с физической точки зрения."

    "Однако я думаю, что они ещё и психологические."

    "И после увиденного утром я запросто могу в это поверить."

    "Знать, что каждый человек будет судить о тебе только по твоему лицу, – это достаточно трудно."

    "Не знаю, смог бы я справиться с подобным давлением."

    "Мои чувства обращаются к спящей фигуре; я встаю и делаю пару неуверенных шагов по направлению к ней."

    "Большая ошибка."

    "Я слишком долго сидел в тенёчке, особенно после столь продолжительной прогулки."

    "После столь резкого подъёма у меня закружилась голова."

    "Это заставляет меня сесть обратно."

    "Чтобы прийти в себя, я на секунду закрываю глаза…"
    
    stop music fadeout 1.5
    
    scene black
    with shuteye
    with Pause(1.0)
    
    scene bg suburb_park
    with openeye

    "Лёгкий ветерок пробуждает меня ото сна."

    "Я протираю глаза и оглядываюсь по сторонам."
    
    scene bg misc_sky_ss
    with locationchange
    
    play music music_tranquil

    "Небо сменило глубокую синеву дня на жёлто-синий цвет раннего вечера."
    
    scene bg suburb_park
    with locationchange

    "Полагаю, все мы на некоторое время отключились."
    
    show hanako emb_downtimid_sun at tworightsit
    with charaenter

    "Лилли ещё крепко спит под деревом, тогда как Ханако, кажется, просто дремлет, сидя рядом с ней, обхватив колени."

    hi "Эй, Ханако, давно ты так сидишь?"
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Н… Не очень."

    ha "Я… я тоже только что проснулась."

    "Она немного ёрзает, и я замечаю у неё за спиной корзину для пикника, собранную в обратную дорогу."

    "Кто знает, как долго она уже тут сидит, ожидая нашего пробуждения, но не желая нас потревожить."

    hi "Что ж, будим Лилли?"
    
    show hanako emb_downsad_sun at tworightsit
    with charachange

    ha "Эм… Я не… Эм…"

    hi "Всё нормально. Не думаешь, что Лилли сочтёт ужасно оскорбительным спать, заставляя нас ждать её пробуждения?"

    "Ханако ненадолго задумывается."
    
    show hanako emb_timid_sun at tworightsit
    with charachange

    ha "Да… Пожалуй…"
    
    show hanako emb_timid_sun at centersit
    with charamove

    "Она наклоняется вперёд с намерением разбудить Лилли…"
    
    show hanako emb_strain_sun at centersit
    with charachange

    "…запутывается в одежде…"

    "…и падает прямо на Лилли."
    
    show hanako emb_shock_sun at centersit
    show lilly basic_surprised_cas at twoleftsit
    with vpunch

    "Лилли тут же просыпается и начинает обшаривать всё вокруг руками, пытаясь понять, что происходит."
    
    show hanako emb_downsad_sun at centersit
    with charachange

    ha "Прости, Лилли! Прости, прости!"

    ha "Я просто… Немножко упала…"
    
    show lilly basic_weaksmile_cas at twoleftsit
    with charachange

    "Лилли берёт себя в руки на удивление быстро, принимая во внимание внезапность пробуждения."

    li "Боже, всё в порядке, Ханако."

    li "Подобные неловкости случаются."
    
    show lilly basic_weaksmile_cas at twoleft
    with charamove

    "Лилли поднимается, держа её за руку."
    
    show hanako emb_downtimid_sun at center
    with charamove

    "Ханако берёт корзину и встаёт рядом."

    hi "Думаю, пора возвращаться, да?"

    li "Да уж, я не отказалась бы принять душ и поваляться в своей постели."
    
    show lilly basic_displeased_cas at twoleft
    with charachange

    li "Не скажу, что спать под деревом очень удобно…"

    "Посреди фразы Лилли теряет равновесие и я придерживаю её за плечо."
    
    show lilly basic_weaksmile_cas at twoleft
    with charachange

    li "Ох, спасибо, Хисао."
    
    show lilly basic_sleepy_cas at twoleft
    with charachange

    li "У меня немного закружилась голова."

    hi "Мне это знакомо."

    li "Не знаю, как ты, но я не представляю, как дойду обратно."

    hi "А как же мы тогда вернёмся в «Ямаку»?"
    
    show lilly basic_listen_cas at twoleft
    with charachange

    li "Что ж, я предложила это место, мне и ответ нести."

    "Не успеваю я возразить, как Лилли достаёт сотовый телефон и начинает кому-то звонить."

    "Пока она набирает, я отмечаю про себя, что все кнопки имеют выступы."

    "Полагаю, это объясняет, как она может так быстро набирать номер."

    li "Здравствуйте. Могу я заказать такси к парку Касанеру? Спасибо."
    
    scene bg school_road_ss
    with locationskip

    "Как ни странно, такси прибывает довольно скоро."

    "Мы втискиваемся на заднее сиденье, Ханако садится между Лилли и мной."

    li "В «Ямаку», будьте добры."

    "Водитель такси" "Будет сделано."

    "Расстояние, на которое утром у нас ушёл битый час, мы проезжаем за несколько минут; и вот мы уже стоим перед женским общежитием."
    
    scene bg school_dormext_full_ss
    with shorttimeskip
    
    show lilly basic_smile_cas at twoleft
    show hanako emb_smile_sun at tworight
    with charaenter

    hi "Что ж, спасибо вам обеим."

    hi "Я хорошо провёл время."

    li "Пожалуйста."

    hi "Спасибо за ланч, Ханако."

    "Прежде чем ответить, Ханако немного краснеет."
    
    show lilly basic_planned_cas at twoleft
    show hanako emb_emb_sun at tworight
    with charachange

    ha "По… пожалуйста."

    hi "Эх, я устал. Жду не дождусь, когда смогу принять душ или типа того…"

    li "Ты совершенно прав."

    ha "Да… Я тоже…"

    hi "Ну, увидимся завтра в школе?"

    li "Буду ждать с нетерпением."

    ha "До… доброй ночи."

    hi "Доброй. Ханако, Лилли."
    
    hide hanako
    hide lilly
    with charaexit

    "Мы коротко киваем друг другу, и девушки исчезают за дверью."

    "Я с облегчением вздыхаю. Не то чтобы мы много двигались, но дневной сон под открытым небом истощил меня."
    
    scene bg school_dormhisao_ss
    with locationskip

    "И потребовались неимоверные усилия, чтобы пройти короткий путь до моей комнаты и в изнеможении упасть на кровать."
    
    stop music fadeout 3.0
    
    scene black
    with shuteye
    with Pause(3.0)
    
    scene bg school_room34
    with dissolve
    
    play music music_gentle
    
    #I've gone back to Playlist naming.
    #BG classroom
    
    "Учитель" "Хисао, вы не могли бы перевести для нас последнее предложение?"

    hi "Эм… «Учитель получил тесты от студентов»?"

    "Я почти уверен, что слышу смешки в классе."

    "Учитель" "Не совсем так. Глагол показывает нам, что это учитель дал студентам тесты, а не наоборот; но ты был близок."

    "Учитель" "Хорошо, дальше…"

    "Смущённый, я сажусь."

    "Выходные с Лилли и Ханако негативно сказываются на моей учёбе."

    "Хотя кого я обманываю; я сто лет уже не учил английский."

    "Стоило мне сбиться, я просто сдавался и всеми силами старался избежать дальнейшей учёбы."

    "Чтение, просмотр телевизора… Пока было что-то хоть немного интересное, английский отходил на задний план."

    "Но сейчас класс мчится вперёд без меня, и, думаю, я должен что-то с этим сделать."

    "Полагаю, у меня нет выбора, кроме как штурмовать библиотеку во время перерыва на ланч…"

    #BG Library
    
    scene bg school_library
    with shorttimeskip

    hi "Э… Привет, Юко."
    
    show yuuko neurotic at twoleft
    with charaenter

    yu "Да? Привет? О, ты Хисао, верно? Это же Хисао?"

    hi "Да, это я. Видимо, твоя память на имена не так плоха, как ты думаешь."
    
    show yuuko neutral_down at twoleft
    with charachange

    "Юко смущённо улыбается; думаю, её память не часто удостаивается комплиментов."

    yu "Ну… Э… Чем я могу помочь тебе сегодня?"

    hi "В общем… Мне немного неловко, но не знаешь ли ты, есть ли в библиотеке учебник по базовому английскому?"
    
    show yuuko neutral at twoleft
    with charachange

    yu "Английского, да? Давай посмотрим… Базовый английский… Базовый… Учебник по базовому английскому…"

    "Юко явно не хватает такта; каждый её «базовый английский» кинжалом впивается мне в спину."

    "Хотя, пока никто не слышит, ничего страшного…"
    
    stop music fadeout 1.5
    
    show lilly cane_surprised at center
    with charaenter

    li "Ох, кто-то ищет книги по английскому, Юко?"

    "Ёлки-палки. Я не заметил, как к нам подошла Лилли."
    
    show yuuko smile at twoleft
    with charachange

    yu "Привет, Лилли. Я просто ищу учебник для Хисао."
    
    show lilly cane_smile at center
    with charachange

    li "Ох, Хисао здесь?"

    "Нет смысла скрывать это…"
    
    play music "bgm/Another_Day.ogg"

    hi "Да, привет, Лилли. Прости, что не заметил тебя."

    li "Добрый день. Никак у тебя проблемы с английским?"

    hi "Небольшие. Мне кажется, я начал немного отставать от программы…"
    
    show lilly cane_listen at center
    with charachange

    #Lilly shocked a little?

    li "Боже мой, но я думала, что у тебя нет проблем с учёбой."

    hi "В естественных науках и в математике – да, но вот английский всё как-то ускользает от меня."
    
    show yuuko closedhappy_up at twoleft
    with charachange

    yu "Нашла! «Английский для занятых людей»."

    hi "Правда?"

    yu "Да, в разделе «Справочники», секция «С»."

    hi "Спасибо."

    yu "Но, может, лучше тебе попросить Лилли помочь?"

    hi "О, а ты сильна в английском, Лилли?"
    
    show yuuko smile at twoleft
    with charachange

    yu "Сильна? Она лучшая!"

    "Сейчас, подумав об этом, я понимаю, что Лилли выглядит так, будто она действительно хороша в английском."

    "В том смысле, что вокруг не так уж много блондинок с голубыми глазами…"
    
    show lilly cane_emb at center
    with charachange

    li "Ох, не глупи, Юко."

    yu "Ты просто скромничаешь."

    yu "Видел бы ты её, Хисао, – половина её книг на английском."

    yu "В смысле, на Брайле."
    
    show yuuko worried at twoleft
    with charachange

    #Yuuko confused

    yu "В смысле, на английском Брайле."

    hi "Думаю, я понял."
    
    show lilly cane_weaksmile at center
    with charachange

    li "На самом деле всё не настолько замечательно, как описывает Юко, но, если ты отстал от программы, я могла бы с тобой позаниматься после школы."

    hi "Правда? Ну, если тебя не затруднит, я был бы весьма признателен…"
    
    show lilly cane_smile at center
    with charachange

    #Lilly smile

    li "Уж не знаю, насколько из меня получится хороший учитель, но я постараюсь тебе помочь."
    
    show yuuko smile_up at twoleft
    with charachange

    yu "Вы можете заниматься здесь. Тут почти всегда тихо, и я попробую найти книги, которые есть также и на Брайле."

    hi "Ты действительно можешь это сделать?"

    #Yuuko Smile
    
    show yuuko neutral at twoleft
    with charachange

    yu "Ещё бы. Многие книги в библиотеке имеются в разных вариантах: на Брайле, большим шрифтом…"

    yu "Скажи название – найду."

    li "Юко часто помогает мне находить книги на Брайле. Выбор тут больше, чем ты только можешь себе представить."

    hi "Это… очень круто. Правда."

    "А я-то думал, что Юко просто недотёпа…"

    hi "Значит, ты можешь читать на Брайле, Юко?"

    yu "Нет… Я просто читаю названия на обложках."

    hi "Что ж, это здорово."
    
    play sound "sfx/chaimu.ogg"

    #SFX Bells
    #Ah, bells. Classic "I can't think of how to continue this" style.
    
    show lilly cane_surprised at center
    with charachange

    li "Ой, а сколько время? Боюсь, мне уже пора."

    li "Ну что, Хисао, встречаемся здесь после занятий?"

    hi "Прямо так сразу?"

    li "А у тебя есть причины откладывать?"

    "Мне в голову тут же лезут тысяча и одно оправдание… Однако именно из-за такого отношения я и оказался в подобной ситуации."

    hi "Нет, я приду. Увидимся после уроков."
    
    show yuuko neutral_down at twoleft
    with charachange

    yu "К тому времени я принесу сюда все необходимые книги, так что обязательно заходите."

    li "Конечно, Юко. Спасибо."

    hi "Да, спасибо, Юко."

    "По улыбке Юко я понимаю, что ей нравится быть полезной, даже если это просто поиск нескольких книг."

    yu "До встречи!"
    
    stop music fadeout 2.5
    
    scene bg school_scienceroom
    with locationskip
    with Pause(1.5)
    
    scene bg school_scienceroom
    with shorttimeskip

    #BG Classroom

    "День подходит к концу, и я собираю свои вещи в ожидании предстоящей встречи с Лилли."

    "В конце концов, с моей стороны было бы грубо заставлять её меня ждать, тем более что она хочет мне помочь."

    #SFX Bell ring
    
    play sound "sfx/chaimu.ogg"
    
    play music music_tranquil fadein 1.0

    "Когда колокол возвещает об окончании занятий, мой портфель уже практически собран."

    "Ловким броском я отправляю в него последний оставшийся учебник и встаю."

    "Несмотря на всю мою подготовку, у передней двери класса уже образовался затор из учеников."

    "Однако задняя дверь практически свободна."

    "Я разворачиваюсь на каблуках и направляюсь в сторону задней двери."

    #Show Hanako
    
    show hanako def_worry at centersit
    with charaenter

    "Проходя мимо парты Ханако, я замечаю, что она замерла и не двигается."

    "Рука всё ещё крепко сжимает карандаш, а взгляд сосредоточен на лежащем перед ней учебнике."

    "На её лице написана крайняя концентрация, но карандаш не шевелится."

    "Мой темп нарушен."

    hi "Эй, у тебя что-то не получается?"

    #Hanako embarrassed
    
    show hanako defarms_shock at centersit
    with vpunch

    ha "Х–Х–Хисао!"
    
    show hanako cover_distant at centersit
    with charachange

    ha "Я… Я тебя не заметила…"

    hi "Всё в порядке, я типа подкрался."

    hi "Тебе помочь?"

    #Hanako looking away
    
    show hanako emb_downtimid at centersit
    with charachange

    ha "Эм…"

    "На будущее: не заставать Ханако врасплох."

    ha "П–пожалуй."

    "Вот же ж… А я рассчитывал прийти раньше Лилли."

    "Но, думаю, я вполне могу ответить на один вопрос и всё ещё успеть вовремя."

    hi "Что именно у тебя не получается?"

    ha "Вот… это."

    hi "Так-с, посмотрим…"

    "Я просматриваю работу Ханако. Маленькие аккуратные символы заполняют страницу, и мне надо всего пару минут, чтобы найти ошибку."

    hi "Ага, вот здесь. Должно быть икс в квадрате, а не просто икс."
    
    show hanako basic_distant at centersit
    with charachange

    ha "А… ох. Теперь вижу. И…"

    "Ханако снова склоняется над тетрадью, вносит исправления и быстро находит ответ."

    hi "Вот, другое дело."

    ha "С–спасибо."

    "Оглядев класс, я понимаю, что мы остались одни и что теперь я совершенно точно опоздал на встречу с Лилли."

    $doublespeak(hi,ha,"Um, Hanako…","Um, Hisao…?")

    hi "Прошу прощения, договаривай, Ханако."

    #ha "D…do you mind if I ask one more?"

    #The choice below is conditional, depending on the attraction points.
    # if(H>(L+2)), then H-path without the choice
    #else if(L>(H+2)), then L-path without the choice
    #else see the choice.

    #If you don't see the choice, then you basically just see what would happen as if you chose that particular line.

    #Choice:
    #1 – Sorry, but I've got to meet with Lilly…
    #2 – Sure (I'm late already)

    #1 feeds into the L path, 2 into the H path.


    #is all of that possible?

    return

label ru_choiceHLT6:
    
    
    #Choice:
    #1 – Sorry, but I've got to meet with Lilly…
    #2 – Sure (I'm late already)

    #1 feeds into the L path, 2 into the H path.
    
    menu:
        with menueffect
        
        ha "Могу я ещё тебя кое о чём попросить?"

        "{font=playtime_cyr2.ttf}Прости, но мне нужно встретиться с Лилли…{/font}":
            return m1
        
        "{font=playtime_cyr2.ttf}Конечно (я всё равно уже опоздал).{/font}":
            return m2



label ru_HLT6a:
    
    hi "Прости, но меня в библиотеке ждёт Лилли."
    
    show hanako emb_timid at centersit
    with charachange
    
    
    
    show hanako cover_smile at centersit
    with charachange
    
    
    scene bg school_hallway3
    with locationchange
    
    "SMSPF" "Ты вышел на роут Лилли! Отправляйся в Лилли, акт 3."
    
    
    
    stop music fadeout 1.0
    
    #"SMSPF" "Lilly route GET! Cut to Lilly act 2."
    


label ru_HLT6b:
    
    show hanako cover_worry at centersit
    with charachange
    
    
    hi "Конечно, я ведь и так уже опоздал."
    
    show hanako cover_smile at centersit
    with charachange
    
    "SMSPF" "Ханабанана! Йо-хо-хо! Вали на Ханако, акт 3."
    
    
    with shorttimeskip
    
    show hanako basic_bashful at centersit
    with charachange
    
    
    
    
    
    stop music fadeout 1.0
    
    #"SMSPF" "Hanabanana GET! Cut to Hanako act 2."
    


label ru_HLT6x:
    
    ha "Могу я ещё тебя кое о чём попросить?"

    return



