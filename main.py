import telebot
import buttons

bot = telebot.TeleBot("6626022302:AAEXN1ZKMb1Vl-ZxrEglyYliAAF8GlcnrK8")


@bot.message_handler(commands=["start"])
def bot_start(message):
    bot.reply_to(message, 'welcome', reply_markup=buttons.more_buttons())


@bot.message_handler(content_types='text')
def bot_answers_to_tect_message(message):
    if message.text.lower() == 'hello':
        bot.send_message(bot.from_user.id, 'I am here to show you text about Kaneki')
    elif message.text.lower() == 'bye':
        bot.send_message(bot.from_user.id, 'return in any time')
    elif message.text.lower() == '':
        bot.send_message(bot.from_user.id, "you didn't say anything")
    elif message.text.lower() == 'who is it Kaneki':
        bot.send_message(bot.from_user.id,
                         "'The main protagonist of the story, Ken Kaneki (金木 研, Kaneki Ken) is an eighteen-year-old black haired university freshman that receives an organ transplant from Rize, who was trying to kill him before she was struck by a fallen I-beam and seemingly killed. After the operation Kaneki develops ghoul-like tendencies and characteristics, and his rationality begins to wane.")
    elif message.text.lower() == 'tell more about his strength':
        bot.send_message(bot.from_user.id, """
Kaneki's mental state undergoes extreme changes over the course of the series. Before his torture, Kaneki would at times refer to his actions as "we" or "us," albeit mostly while in a stressed state. Kaneki personifies his feelings to an extent that they take the form of people existing within his mind. When meeting these mental constructs, Kaneki enters a limbo-like state where he converses with them. Kaneki initially only entered this state when he was under extreme duress or near-death and later included during calm settings for conversation.
During his torture at the hands of Yamori, this construct takes the form of Rize Kamishiro. She taunts him for his weakness and shows memories from his past with his mother, forcing out his anger towards her for not being able to refuse her sister. Through these memories, she gradually convinces Kaneki to abandon his previous ideology of being the one who gets hurt instead of others. By accepting "Rize," Kaneki embraces a more brutal view of the world and accepts his ghoul powers.
The next time he encounters this alternate self is at V14, after being mortally wounded by Arima. Within his mind, he encounters a child version of himself that he feels the desire to protect. As he comes to accept his failings and similarities to his mother, this self transforms into a version of Kaneki as he existed at the beginning of the series. This more innocent Kaneki accepts him and thanks him for all that he has done to protect them. The two vanish together, resolving to "sleep" for a while.
In Tokyo Ghoul:re, the mental construct took on the appearance of Kaneki, initially appearing as Yamori's prisoner while donning his kakuja mask. This "Kaneki" torments him, demanding to be accepted and given back his body. Sasaki denied this being, which leads him to moments of instability whenever he uses his ghoul powers. When he is finally forced to accept his past and honor the request to "look" at "Kaneki," the projection appears to him as a white-haired child who he feels the need to protect. In the months following, Sasaki and "Kaneki" regularly converse with each other. Unlike previous constructs, Sasaki often imagines the child in the real world, picturing the child going through normal activities such as reading. Though they have reached an understanding, the child "Kaneki" tells Sasaki that the two of them cannot continue to co-exist and one will eventually vanish.
During Sasaki's fight with Karren, a heavily injured Sasaki once again retreats to his mind. The child then confronts him, taunting Sasaki for not being able to protect himself. Sasaki attacks the child, which prompts him to unsuppress his memories of being abused as Kaneki. As these memories came back to him, the child expressed that Kaneki was trying to die during the events at V14. He also desired to be loved by everyone that knows him, regardless of how his actions may obtain the desired result, be them with good or bad intentions, which the mental child Kaneki perceives as salvation. Sasaki regards himself as a "dream," caused when he began to desire. After Sasaki accepted his past, he resolves to quit "dreaming."[21]
During Sasaki's fight with Arima at Cochlea, the latter savagely beats him to the brink of death. As Sasaki was about to succumb to his injuries and die, his mental construct takes the form of Hide. "Hide" scolds him for his selfish excuses, deducing that Sasaki had heard the sound of the compactor and asked whether he was okay with seeing his friends dying and letting his efforts be in vain. "Hide" encouraged Sasaki to live, reminding that he sacrificed himself with the goal of "living together with him" and that living would allow Sasaki to find a purpose in life.[22] Sasaki's appearance begins to revert back to his post-Aogiri days, with his hair becoming white again.
"Hide's" advice made Sasaki realize that his mental constructs of "Rize" and "Hide" were all just manifestations of his inner desires and thoughts. Sasaki believed that Hide would stop him if he went beyond his own boundaries, causing Sasaki to deduce that once he began to think this way, he began to desire to live again.
When reduced to only his body and head after being beaten by Juuzou and Abara, Kaneki once again retreats into the inner recesses of his mind. His different personalities convene and discuss what went wrong and what they should've done. Eventually, his many personalities begin to argue and the situation erupts into chaos before they all realize that they have one thing in common; they need to save Touka. Upon this realization, Kaneki asks himself under the guise of his various selves if he's willing to cross the line of killing humans and children. In response, he declares that he will, and that he'll "press forward, like a centipede".
While Dragon runs rampant throughout Tokyo, Kaneki remains comatose within its recesses. In his mind, he finds himself in a shrine surrounded by an endless ocean. Upon diving in, he finds the bodies of his victims drowning beneath the waves. As he surfaces, he's greeted by "Rize", who asks him if he remembers the first time they met. While Kaneki doesn't regret meeting Rize as he's met many friends along the way, "Rize" states that she hates him as she'd never be reduced to her current state if she'd never met Kaneki at Anteiku. As he's being pulled out of Dragon, his mental world begins to collapse, and Kaneki leaves declaring that he'll try to bear the weight of his sins.""")
    elif message.text.lower() == '':
        bot.send_message(bot.from_user.id, "you didn't say anything")




    else:
        bot.send_message(bot.from_user.id, "you id was copied")





#
# @bot.message_handler(commands=["come"])
# def start(message):
#     user_id=message.from_user.id
#     peremennaya=bot.send_message(user_id,"assd", reply_markup='knopki')
#     bot.reply_to(peremennaya)
#     bot.register_next_step_handler(message,sled_funksia,peremennaya)
# def sled_funksia(message):
#     pass


bot.infinity_polling()
