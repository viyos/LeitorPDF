from tika import parser
import pandas as pd

for i in range(10000):
    try:
        if i != 0:
            read = parser.from_file(rf'Votaçao_Assembleia_PLR.docx ({i}).pdf') #Entrar num looping com os nomes dos arquivos PDF
        else:
            read = parser.from_file(rf'Votaçao_Assembleia_PLR.docx.pdf') #Entrar num looping com os nomes dos arquivos PDF

        read = read['content'].strip().replace('\n','').replace('_','').replace('\t',' ').split(' ')

        i = ''
        while i in read:
            read.remove(i)

        resposta = read.index("X") #Index do SIM,

        if resposta == 100 or resposta == '100':
            respofc = 'SIM'
        else:
            respofc = 'NÃO'

        nome_completo = read[104:len(read)-5]

        separador = " "

        nome_completo = separador.join(nome_completo)

        cpf = read[102:103]

        cpf = separador.join(cpf)

        lis = pd.Series({'Resposta': str(respofc), 'Nome': str(nome_completo), 'CPF': str(cpf)})

        df = pd.DataFrame([lis])

        if i == 0:
            df.to_csv(r"Votacao_Assembleia.csv", index=False,sep=';',encoding='utf-8-sig',mode='a')
        else:
            df.to_csv(r"Votacao_Assembleia.csv", index=False,sep=';',encoding='utf-8-sig',mode='a',header=False)

        print(df)
    except:
        pass
