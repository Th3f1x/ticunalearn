def sub_line(line):
    if line.strip() == "TORÜ DUǕ'ǕGÜ":
        return "NOSSO POVO"
    

    elif line.strip() == "Nori arü ügü ga ore ga nucüma'ǖ ga torü ga na nhunhaacü yi'i'ǖ.":
        return " Aqui começa a história do tempo dos antigos "
    

    elif line.strip() == "Norü ügü tchiga":
        return "O início da história"
    

    elif line.strip() == "/// 01 Nüma ga Ngutapa ga naãne nama'ã ya ĩĩtchicü, ":
        return " Antes do mundo existir, ///02 Ngutapa já existia. ///03 Ele não teve pai nem mãe. "

    elif line.strip() == "/// 02 rü nge'eǖ rü na tauma i ta'acü i nhũma na yema i na i aẽǖrü'ǖ. ":
        return "04 Mapana, ///05 a mulher de Ngutapa, ///06 se criou junto com ele. ///07 No mesmo lugar viviam também Baia e sua mulher. ///08 Baia era parente de Ngutapa."
    

    elif line.strip() == "///03 Rü yiĩ'ǖ ngema na yamareǖ ga Ngutapa. ":
        return "09 No lugar onde esses quatro se criaram é onde ficava a montanha Taiwegüne, ///10 E no igarapé Tonetü. ///11 Naquele tempo, ///12 a terra ainda estava se formando. ///13 O mato era baixinho e o rio ainda tinha pouca água, ///14 lá eles viviam. "
    

    elif line.strip() == "/// 04 I nori'ǖtchicü, ":
        return " Passaram-se muitos anos. ///16 Ngutapa e Mapana nunca habitaram juntos. ///17 Nunca tiveram filhos."
    

    elif line.strip() == "/// 05 ingeguma, ":
        return " Um dia, ///19 quando o mato já estava crescido, ///20 Ngutapa foi caçar com Mapana. ///21 No caminho eles"
    

    elif line.strip() == "/// 08 Erü nüma ga Baia rü Ngutapa tanü'ǖ ni'ĩ rü wü'iva na yae.":
        return " Então apareceu o pássaro cancã e se sentou no alto do pau onde ela estava amarrada. ///30 Mapana disse para o cancã:"
    

    elif line.strip() == "/// 09 Nucüma ngeguma rü numa ga Ngutapa rü na tauǖma ga norü bue nu'ǖ tayema yerü tauguma nügüga nidau, ":
        return " - Vovó, ///32 pode me desamarrar?"
    

    elif line.strip() == "/// 10 ga namamaã rü na yaemare. ":
        return " - O pássaro gritou: "
    

    elif line.strip() == "/// 11 Ngeguma yema namamare i ya'ĩ, ":
        return " - Co, co, co, cou! "
    

    elif line.strip() == "/// 12 rü tauguma i buǖã. ":
        return " - Vovó, ///36 venha me desamarrar. ///37 Aquele desgraçado me prendeu aqui para me matar ///38 - ela falou de novo. "
    

    elif line.strip() == "/// 13 Ga ngĩma ga Mapana, ":
        return " O cancã se transformou em gente e, ///40 chegando mais perto, ///41 perguntou:"
    

    elif line.strip() == "/// 14 rü yemaca ngitchi naai ga nüma ga Ngutapa.":
        return " - O que lhe aconteceu, ///43 minha neta? ///44 Se você quiser se vingar de Ngutapa, ///45 está aqui a caba."
    

    elif line.strip() == "/// 15 Inacü i ngeguma i ngema. ":
        return " Ela pegou a caba e guardou."
    

    elif line.strip() == "/// 16 I Taiwegüne i nori naãene i üǖwacü rü ngema ni'ĩ i nangemagüǖ erü ngema i nori naü'ǖ i naãene nua natü i Tonetü.  ":
        return " A casa de caba era muito grande, ///48 mas parecia pequena. ///49 O Cancã falou ainda: "
    

    elif line.strip() == "/// 17 Erü yeguma ãrü naãenecü rü wü'i i ngewaca i ya eaneǖrǖ'ǖ ni'ĩ yerü natauma ga nhãtü rü yema nawa nayemagüǖ ricatama ni'ĩ.":
        return " - Você não pode ficar aí. ///51 Tem que esperar o seu marido num lugar onde ele não possa ver.///52 Depois disso, ///53 o cancã se transformou em pássaro e foi embora."
    

    elif line.strip() == "/// 18 Rü yeguma ngemamã ni'ĩ i nangemagü'ǖ, ":
        return " Demorou um pouco e Ngutapa voltou da caçada. ///55 Vinha tocando flauta e pulava numa perna e noutra, ///56 cantando: "
    

    elif line.strip() == "/// 19 rü marü nhurema ya taunecǖ na yemagü rü yegumama ni'ĩ ga tüǖ nacuaiǖ ga namã ga Ngutapa rü yeguma rü na tauma ga to, ":
        return " - Por onde anda Mapana?! ///58 As cabas e as formigas morderam a periquita dela! ///59 Tcheruru tcherμru-u-u-u ... Tcheruru tcheruru-u-u-u ... - assim dizia."
    

    elif line.strip() == "/// 20 ga duǖ'ǖ nüĩcagümare ni'ĩ ga nayemagü'ǖ. ":
        return " Mapana estava escondida num tronco de árvore, ///61 esperando Ngutapa passar. ///62 Escutou esse canto e se preparou. ///63 Quando ele chegou, ///64 ela jogou a casa de caba em cima dele e acertou-lhe os dois joelhos. ///65 Ngutapa caiu e não se levantou mais. ///66 Mapana deixou ele ali mesmo e foi embora."
    

    elif line.strip() == "/// 21 Natürü ga guma Baia rü nü'ǖ tayema ga bue rü naaãcü nǖetcha nüma ga guma. ":
        return "Ngutapa foi se arrastando até em casa. ///68 Desde que as cabas ferraram, ///69 seus joelhos começaram a inchar."
    
    else:
        return line.strip() 

def process_input():
    translated_text = ""  
    last_line = None  

    while True:
        line = input()  

        if line.strip() == "" and last_line == "":
            break

        translated_line = sub_line(line)  
        
        translated_text += translated_line
        
        last_line = line 

    if translated_text.endswith("///"):
        translated_text = translated_text[:-3]

    print(translated_text)  

process_input()
