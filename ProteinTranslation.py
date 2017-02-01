# Works!
def read_codon_table(filename):
    codon2aa = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split()
            codon2aa[key] = val
    return codon2aa


"""
Given a sequence of RNA, translate it into Proteins using the Codon table

"""
# Works!
def ProteinTranslation(seq):
    protein = '' 
    codon2aa = read_codon_table('Codon_Table.txt')
    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        aminoacid = codon2aa[codon]
        if aminoacid != '*':    # * is the Stop symbol
            protein += aminoacid
    return protein


def test():
    in_ = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    out_ = 'MAMAPRTEINSTRING'
    assert(ProteinTranslation(in_) == out_), 'Test 1 FAILED'
    in_ = 'AUGCCCAUGGGAUUAGUGUGGCACAAACAAGGACCACUAGAAAGGAUAUCUAUAAGAGGAGUAAUAGGAGUUAGGAGCGGGUAUAACGAAACCAUUCGAAGGAAUUGGGUCAUGUUAGUAAGUAAAAGCGCCUUAUUCGUAUCCACAUGCUGCCAAUGUAACCCCCCUUACCUGACUUGUUAUAAGCAGUUGAAGAGUCCAGACGUGACACGUUUUGCGCGCGCUCAUGACAUGGAUCAUUUUAGAGACCACACUCAUAUGGCUGGGAGGACCAACUUGGAACAAACGUUUUGUGCUCAACCCGUACAUCUGACUAUGGACCUAGAGUAUUAUCAGGACCCUCCAGUGGCUUAUGUACUACAGUACAUGGUGCCGAGGCGAAUGCCAGCUCUGUCAGUAAUCACGAAUCCUCCCAACCAAGAAUUGCAUUCACUCUGGUCAUAUCUGCAUUUGUCGGUUAGUCAAAUCUCUCGGGGGCGUCUAACUUGCGUGACGCUGCUACUAGUGAUCUGGGACAACCAUUUAUUACGGUACUCCUAUCUUUGCCAGGCCUUCGAAAUGGUUAUGAGCUCGAACAUCCGCUCCUUGGGAGCUGAGACGUUAAAGGUGUUAACAGAUCCGAAUAGAGAGUGCGCUUCGGUCACCAUCCCACAUCUCACUCAGCAAUCCGCUCUGAGUAUUAGAGCACCCCCCAGGUACCUUCACACUGAAUUACGGCGUUGUAGAACAUCUUUAGCACGGACGACCCUUCGGUUCGUGUCCAGUUGUACCUCUCGAUUUGGUGCUUCGAUUCCGAGCUUUCAUGAACUCUACUGCUCGCUAUACACAGGGCUCUCCUUCGUUCAUAUAUCUCGAUCAAUUAAGAACGCGGUUGAUCAAACAUGCGGCAAACCUAUCGACAAUACUCAGAUUGUGAUAAGCUUCCAGAGCUCUCGUCUCCAUCGAUGCAGUCUCAUAGCUCGUCUACAGGCCGACCGUACUUUCUUCCUUUAUAAGCGAGGGUGGUGCCGGGGCGUGUGCUCUAUAGUUAUAUACUUGACCGGGAUCUGCUACGUCAAACUGUGUUGUUACGCUACGGGCAUUAGCACCGUUAGCGACAGCUAUAAACCAAGGGGUUACGUUCAUCUUCAGGUAUUUCUCUUCCGACACGUGACUGUGUACGUAAUUCGUACAUAUGAGAAUUCAGUUACCGGGGCUUCACGAUAUCAAGCGGACUACAUCAUGGGGCGCGACUUACCUACUCUCGUAGAUAGUUUGCCAGUGGUGUCGUAUAGUUGGAACCAGUACCUGCUUCUAGUCUGUGGACCACGUCGGGGAGACCUCUUAUGGCCCCUAUUAGGCAGGGAUCCAACAGUUAAAUUUAAACCGCGGACCUACCGUCAACGGAGGAGUUUUACAGCUUUCAUGACGCGGAAGUGCGUUUCACUAUGGGCGCAAUUGACAGCUCGCCGUCGGACAAGCCGCAAAUUAAUUCGGGCACUAACUCACGGGUGGAAAAUGCGAAUGUCAAGACACGCAGUGGUCUAUACAGGCAUAGAGGGGAUCCUCGGGUCGAAAACAGAGUUAACGGUCCCAACUCAUCCGCUGUACAUCUUGCUCCCGUGCUCGGGUCCAAGUUGCGUGCUCAUGACUGGGGUCCGACCAUUUUGGUCUUCGUCCCAAGAUAGUCGUUGGUCAACAACCAUCAGGCCGGAGGGUGGUGUACUGAGCGUAAGUUGCAGACAGAUAGCCAAUAGCACCUUCUCGGUGCUCGAGUCAUUAGGUCUCUUUAUAGAAGUUCGGCACGGCCACGGGAAAAUCCCGCUCUACCGUAGCUCCACCUGUAGUAAUUGUUCACAUGUCUGUCAGUCUAAUGAGUGGACAGCGUGGUUCUUGAACUCCCCUGCGGCCGGGCCGAACCAGUGCCAAAUUGUUUAUAAUACGAAAUACUGUAUUGCAGGGUACGCCCCGAGCCCGUUACUAAGCACAGCCCGCGCAGCGAGUUAUCGAUAUAAAUGCUCGUGGUACUUCCUUCUUCUCUUUUUGACGUGUUCCCUCAUCUCGGGGCAAUUCUUGGAACCGGGGAUUAUGAAGUGUGCACUGGGCAUGCUAAAGGUAGGCUCGGAAUGCAAUCUCGAUGAACCGCACGUUAGUUCCACCGCGGGUUACCACGGCCACGUGAACACCCUCUGUUGCAUUAUUGCAGUUAGCCCGCCGCUAAGCCUGCGGGUUAAAAGACCGGCGGGGAGAGUUGUCUUCGAAAUAGGUCCCGCAUGUGAUCAGGACGGUGGUCAACUUGCGUCAAAUAUAGUGAUAACUCGUAAUCCGACUGGGUGGCACCCAUGGACUUCCCGAGUCAGCGCCCUUACCAUACGCUCACUACAAUGCCCACAGUGUGUGAACGAAGGCUGGCACUGGUCGCACCCUGAGCCAGGACAUAUGGGACGAUACUUGCACCCAAACUCAAUCCCUUACGAAGCCUGCGUCUCUACCUAUACAAUUGCCGAAAAAUUCUCGGUUCAUUUUAGUACCCGGAGCAUUGACUGGGAGUGCCCGGUCCGAAUACUCGCGACGUACACAAGACAGCUGGAGUUGCGUUGCCUUACCGGAACGUGCUUUUCCUACUGGAAUACCCCAAAGAUUCCUACGGUAACACCCCAUGUAGCACGGAAAUCUAAGGAGACUGACCGAAACGCCUCGAUUCAGCCCCCGAUGGCUGCUACGGUACCAGCAACAGGCUUAUCGAAGCAAUGGAUUGUCAUCCAAUCUUCCAGGGAUCUCCGGACUGACGAUGAGAUGGAUACCACCUUUCAGACACAUCGGUAUGGCUUCGGAAUAUCAACAACGGAGUGCUACACUCUACCGAGCCUAUACUCUGCCCCAAAGAGUAGAAAUACCCACACUUGUCACGCAUCGCCUUCCAACGAUAGUUGGUCCUGCUUCAAGCUCUGUGGAGUAAGUAUACGUGAUAGGAAAAGACGAGUCUGGACUGCUUCGCGAUGUAAUGACCUAGCGUCAGAAAAGGGUGGCCGGCAUGGUACACCACCCACAAGAAUCCCACCGUCGUUGCCUAGAAAAACGACACAGACUGGUGCAGCGAACCUAGCUUACUGGUCCCAGUUCAUUAACGGCGACAAAUCGCCGGAUGGCUAUACUAAGCAUGUUGGCACGGACGCCAUAUAUGCAGCGCGUGUUCAAGCGCACAGCCUGACGUGCUCCCGGCUAUCCAGAAUUGUGUGUAGUGGAUCCGCCGUGGGUUGGGAUGGAGACGAUUUUCGUGAGUCGGACGUUGACCGAGAAUGCGAGGUUACGAGUGGCCCAAGGCCCCAGAGAUUUUGUAUUUACAUCAUGUCCUCCGUUUCGACCGACGGUGGAGUAUGUCGAAAGAUCUGGAUAUUCCACCUCUUAUCCAAUUCAUGUAGGAGCUUGUUUUCCCCGUCAUCAGAUAGGGAACAGAAGCUCGGAAUAAUGGCGCAGGCAGAGGUGUUCUGUCACGCCCUCUCAAAAUUUCUGUUUCGGUUGUGUUCUAUUUCAUCGCUCAGGGCGCUCAGUUCUUAUCCCAGAUCGGGGCGAGUUCUCUCUAUUGUGACAAACAUACCGCAGUGGGACAGCCGCCCUAGGCUACGAAUUGACUACCAUCAAUUUACACCAAUUUUUCAUAACCCGCCAGGUAAACUCCUGCAGCCUAACGAUACGUGCCUGGGCUGUUCAAACUGCCUCCAGAGCUCGCCUCUGCUUUUUACCCGGGCAGGUCUUUUGGGCCUAUUCAGAACCAUGGCCCCUAUAACAUACGGCUGCAUGACUCGCUCUGCUUGGUCUUCGUUACAGCGUGGAGGGCCACUCGACGUUAUCCUCUCUACGUCGAGAGCUACCCUAUUCAAGCGGUGUGUAAGAUCACGAUUCAGAAAUCCAUGUGGUAUUAAUGUUCUCACAAACUUUCACGAACCGCGAGCACUUCUAUUUAGCGCUCCACGCGGGAAUCCGAGCUAUACGGUCAUGUUCGCCAGUACGGCAGCCACGUGCGAGCGCCUGGCGUUAGCACGUCAUCGUACUUAUUCCCGAUUCCUCUUUGAACGUACUAGAAAACAUGCGCUGAAAGGGAGAACAAGUGAUCAAGACGGCCUAAGUGCCGGUGUCACGUGGAAGGGCGUGAAUUCUGGCCGGUACCUUUAUAGCACGUGUCGUCAUGGGCUGCGCAGGUUGAUCCGGACGAUGAUGAAGCAAAUUGGAAGACUAUUUUAUAGAACGAGGUGCACGCUUCUCGUCCACAGAGACCCUGGCGCGGAACACUACCUUAGUACGCCAAUAGUAAAGCAAGGACGCGGCUACCACCGGCGUACACGACUUCCAUUUCUGCUUUUUUACGACCAAUGCCCAGCGCGCGGAGUGCCGCUAUUAGUACGCUUAGUGACCAAUGCUUUAUCGCCUUAUAUUACCAUGUCAUAUGCAUGUCAGACUUGCAACAGAGCCCAGGAGAGCGUCAGCCUAUUACCGAGUACAUGUGCUUACCCCUACCGGUCAAUCAAUUCCGAUCCUGUUGGAGCUUGGAAAGUGGGCUCCCUAAAUACGCACUACAUUUGUAAGUUACCCAAGGUAUCACCGCCGAGAUGGGCAAGCUCACAGCAUAUCGCGAGCACAGUCGUUAGAAGCGAUACCCAUAGUAGAGACGAGUCGAUCAAUGGACAUGGCAGGCUUAAAGUUGCAAUCAUUGUUUGUAGGGUAACCGCAAGAAGUGUAGCAGAAGUCGGAGGUUACUGGAAAAAAAGACACAGGAGUCCACGAAGUAUAUUUGAUAUGAAAAAUAGAGACACUUGGCACGAUGGUGGGCGCGGCCCUACAUCAUCGUCGGACCAUUAUUAUCCCAUAACAGGCAUUCCUGUUCUCAGUACUCCCUCCCGGAGGCCUCAAGCUCGGCUCACCAUUAAAUCGUCAUCAAUUUGGGCUUAUCGAGAUCAACCGAUGCUCACACAGCCAUGCAUUACGUACCCGGUACUGCUCUUGCAAUGGGCCGUAGCUUCGCGAAUGAGUGCAAUAUCUGGCAUUCGGCUUGCGGGUCUGUGGGGAGCAGCUAAUGCACCAGUCCAACUCUUCCUCUACCUCAGUCAGUGCGCACACUUAGGAACUUAUUGUGUAUAUCACGAAAUGGGCCCAAUGUAUAUGGUUCUACCAAACCAACGGCGACUGCGACGCUUUAGUCUUGGAGGACAGAUUCUAUGUUACCCCUUCAGGACGACUUACAGUCGGGCUGUCGUUAGGCCUUAUCCUGAUACGCCGCAUGGUUACAGCGGUAACGGCGUAAACACCGGCUUCCUAAGACGCUGGCCUGGACCUGUCCCGUGUCUGUGGGUUAAGGGUGUUGCCCACCACGCGUCUAAGCUACGGUGGAAGACACUUGCUUGUACUGCGUUAUCCCUGCCUGCCCUACCUAGUCACCCUGGAUUAUUGAAAAGCCUUCUCAAAAGAGGCGAAGUGAAAAAACUGGAGGCAGCUCGCACCGUCUUGCGAGCUUUACAACCGCACCGAACAAAUGGCGGAUAUACUAAGGAACUCGGUCAGGAGGAGGAGCACUGGUUCAGGUACUCAUUCGGAGGUACGAUCGGGGCCUUGUACGAUCGUAAGGUUGCUGUGUGGUACCGCAGCUCACAGGUAAUCUACAAUGGUCCUAUUUAUCGUCUAGUACAGGAGCCGAGUUGCGCCUCUCCGAUCACCUUAUUCAGCCGAGUACUACUUAAUGUUGUAUCUUAUCUAGAGAUAACGGUUAAACGACAUCUGUUCACACCAAACACCAUCCCCGGACGAGGCCUUUCUCAUCGAAAGGGGGCAUUAUUUUUCCUAAUACCACCCUAUCCAAGCUCGUUCGAAUUAAUAAGAAAACCCUACCGCCGCACACAGCCUGCUUUUCCGGGAUCCCUAGGCGAUGAUCCCUUGCUCCCCUGUAUCUGUCGGUCUAAACUGCGACUCAGACGGAUAACUGUGUAUGGUUCAAGCCGGCCAGUUGAAGACGUGGGAACCACGGAGUCUAGAUGUCCAAAAACAUUUUACUCUCUCCCGCUCGCGCUGUGUUGGUGCCGGAGUACGGGGGUGGGCAUCUACGGCUAUCUGGAACCGGACUACCCGUAUUAUACGAGGCGCGCCCCCGCCAUACCAAUUUGGAGACACCCUGUAUAUCGCGCUUUCGUACAGUUAACGUUAGCGCAGGCGACGGUACCCGGGCCGAAGCCGUUUUUAUUGCUACCCGUGGGCACCGGACCGUUUAUAAAAAUUUUCGGCCGCCACGGUUUUGCAGUUUUAGCUGCCGUACGAUAUUGUACGCUGUGCUCGGACCCUAUACGGGGACCCGACAGCCGACUUAGCCUAGUAACAGAGAGUGCUCGCCAGGUUCUCACUCCGGUCGAGUAUACCGAUCUGCAACUGUGUUCACUGGGGAGCAUUCAAAAGUCAAAACGGCUCUCAAGACUAUCCCUAACCAAAUUUGAUGAAUUAGCCGCCCGAACAAAUGCUCGGUUCGUGCGUCCCGUAGGAUAUCAACAGGUUAAGCCCCGGGUGAUUGAAACUGAAACUCCUUAUAGGACGUAUCGGCCAAACCCGCCUACAGAUGUAGACGAGGAGCACAAACAUCGUUUACUAGCUGUCAAAAGAUACAUAGGUUUCAGAGGGACACUGUCGGACAGACCCCAGGCGGCGCUCAUUAAAGGUGAAUGCAAGGCCAGCAGGUCGGGGCAUCUUCUUGAAAUUCAUAGAGGAUCAGAGAGACUUGAUUGCCGUAUCACGCUAACGCUACUUAAGGACCCACUUGGCUACUUUUACGGAGUGGACAGUCAGCCACCGGCGGUGCAUUUGAGUUACGACGCGUUCUCGCAACUCAUCAAAAACAGAUGUUUUAGAAAUUACAAGUCGCGAGCUUUCCAAGGCACAAAUGUAGCACGAAAAUCAAUAUGGGAUCGGUCAAGUGACCCUGGUUUGAGGGAGCCAUUGUGUUGGACACUAGACAAGCGCUGGGCCAAGUACACACAUCAACCUCAACCCUGCCAGCCGGUUCCCACCUCCAAUGUAUUUGAAUGCAGGCGUGGCCAAACCGAGGUACGACAUAACGCGUUGGUCUAUAGUCCAACCUUCGCGAAUUUUCGUGUAUCAGCGGACAGUACUGUCUUACUUCCAGCCACCGGGUCAUUAAUCGUUCCAUCUGGAAGGUCCGAGCGUAACCCGGAUUAUCACGCGCCGUGCUCUUUAUGUCCCAACCUCAACUCUGGUUUGCCGGGUAGGAUAGUAGGGACGCCUCGAACCGACAAGCGGCGGGCCGUCACGCAACUCAGGGUGUCCGAAGCAAGUUGCCCUCAGCGGAAUAGAUCGCCUGACUCGUGCGCACUAGGUAAAUGCCCGCUUCCGUUAGAUAACUCUACAAGCCGAUUUUGCGGCCCUUGCGCACAUUAUUCAGACCUAACCACAUUUUUACGGCUCUUAUUCUCACAGACUUCGCCCGAUGGCAGGUUUUUCCAUCAGAUAAUAGCGGUACUCAAAGUGGGUAAAUGCAUUAGAGCUACUGCAGCAUUGAACCCCGCCUCGUACCUUGCCAGCCGUGCUGCACAGUCUGGAAAUAUUGUGGAAGGUCAUCGGGGACCGAUUUUAAGCAGGAGCAUGCUAGUAAAGCGAAACUGGCGUUGUCACGGGUCCUUACCAUGCAAUAGGACGACGGGAGAAACACUUACGAUAUUAGGCAUAAUGUACGGAUCCGUGGGUGGCUCCAGAAUAUUACAAGCAGUAGUGCAUUCGGUGGCUAGACGCGCCCCGCAGGCGACCGAUGGUUUUGGGCAUUUGCUGACCAAACCGUUCGUCAGAGCCAGAACAUCAGAAGAGGAUAAAGGGUGGGUGGUGACUUCUAUAUUCCCUCGACGGAACGCCUAUGACCCACUCGGUAAAGUGGGCCCAACAUGGCGUACGCCCGGCUAUCGCAUGAUACCUCAAGCAGAUAAGUGGGGGAUCGGACCGACUAACGGUGAUACAGCCAACUGCGUAGGCGGGUGCCUCAGGGUAAUUUGCCCGUCCAGGGCAUCGAAGCAUCACGCAGCAAUAUGCUUAUCCGGCACAAGCUUCGCACGUGUGGGAAAAGGAAGAGAGGAAAAAGUCCGUCAUACGGAGUCCCAAGCGUGGACACGCUUUAAUCUGGGUAAUGCGAGGCGAGGUGGGGUGGACCAGAUUUUACGGAAAUUAACCAUCGAUAGGGGUGGGCUACGUGGGCACGCGAGGAUAAGUACGAAAUACCGGCCCCGCCUACAGAGGAAUGCCACAAUGGCCGGGAAGGAUACCCGACAUUAUUUGAGUGCUUUCAAGUUCGAACUUGCCACGCGAGCGUACAGAUCGGCGCUAAUUCUCUGGGAACUUAUCCAGAGGAGUACUAGAACGCUGGCUUAUUCUACGGGGCGGAUUGAACUCCCAACAACAGUGCCCCACUCUUCGCCCGGUGUUGUGCUAUUAGGAGUAGUGAAUUUAAGAGGAGAAGCCACACAGCAUGCCCUAUUCUCCUAUCUGGAUUCUACUACGCCCUAUGAGUGCUUAGACAUAGCCCCCAAUAGCUGGUUCACGUCCGAGUCAUCCUGGCCACGUAGCGAUGCAAUACUAUCAUACCGGUUGGUUAAUGACCCGGCUGAACUUCUUAGUGCAGGGCCAUCAACGCUAUCACACCCGCUCUGCGGAUCCAUCGGCCGCUCCUUAACACGAGGAGACAGAUUAACGAAGGACUACUACGUAGUACACAAUUUGAGCUCCUCGCUUACGCGAUUGGACCGUCAUAGUUCAGCGACGCGCAGCUUGCGACCAUGCCUGUGGGUCACAACAGAAAAUACAAUUUAUCUUCAGAGGACCUGUUUCUAUUCUGAUUGGGAUUGUAUGCGGUGCCUUUCAGACAAGGGAGGCUACGAUGGCAAUUAUUCGAGGGUAACCGCUUAUCACUAUUGUCGGCCAAAAGUUCACGAUGAGGCUACAGUGUUAUACAAACUUAAGGGUACCCCCAUACGAUUUGGUCCGGCACACAACCACAGAGGUGCCUUAGCUCUUCGUCCUGUUGAAACCACCCCCCUGAGGACAUCUCCUGAAUAUGUGGAACACCCUUACGACGAGGAGUCUAAUACAGGUCGGGGGGCAGCUCGGCAGGAAGGGCUCGAAGUUCAGCUCAUUGCAGGCCAGUACGACGCUUGGCAAUGUAUGGAUAACUGGACGGUUCACAUCAGUCGACUAUGUACCGGGGUACAGUCCCCACCGUUGGCUCGUAGAGUGUCCUAUUUAGGAAUCAGUCCGGACAUUUGGGGCCAUAGUUUUAGUUUCCGCUACACUUGGCCCUUCAAAAGCUCGACCGGGGCGAUUGAUUGGCGCCACGGGUUGUACUCCUUCCUGUCUACCUUAAUAAUCGGUUGCUGCUCACGAGCUCUGACUGAGAGAUCACGUCGAGGACCAGCCCGUUAA'
    out_ = 'MPMGLVWHKQGPLERISIRGVIGVRSGYNETIRRNWVMLVSKSALFVSTCCQCNPPYLTCYKQLKSPDVTRFARAHDMDHFRDHTHMAGRTNLEQTFCAQPVHLTMDLEYYQDPPVAYVLQYMVPRRMPALSVITNPPNQELHSLWSYLHLSVSQISRGRLTCVTLLLVIWDNHLLRYSYLCQAFEMVMSSNIRSLGAETLKVLTDPNRECASVTIPHLTQQSALSIRAPPRYLHTELRRCRTSLARTTLRFVSSCTSRFGASIPSFHELYCSLYTGLSFVHISRSIKNAVDQTCGKPIDNTQIVISFQSSRLHRCSLIARLQADRTFFLYKRGWCRGVCSIVIYLTGICYVKLCCYATGISTVSDSYKPRGYVHLQVFLFRHVTVYVIRTYENSVTGASRYQADYIMGRDLPTLVDSLPVVSYSWNQYLLLVCGPRRGDLLWPLLGRDPTVKFKPRTYRQRRSFTAFMTRKCVSLWAQLTARRRTSRKLIRALTHGWKMRMSRHAVVYTGIEGILGSKTELTVPTHPLYILLPCSGPSCVLMTGVRPFWSSSQDSRWSTTIRPEGGVLSVSCRQIANSTFSVLESLGLFIEVRHGHGKIPLYRSSTCSNCSHVCQSNEWTAWFLNSPAAGPNQCQIVYNTKYCIAGYAPSPLLSTARAASYRYKCSWYFLLLFLTCSLISGQFLEPGIMKCALGMLKVGSECNLDEPHVSSTAGYHGHVNTLCCIIAVSPPLSLRVKRPAGRVVFEIGPACDQDGGQLASNIVITRNPTGWHPWTSRVSALTIRSLQCPQCVNEGWHWSHPEPGHMGRYLHPNSIPYEACVSTYTIAEKFSVHFSTRSIDWECPVRILATYTRQLELRCLTGTCFSYWNTPKIPTVTPHVARKSKETDRNASIQPPMAATVPATGLSKQWIVIQSSRDLRTDDEMDTTFQTHRYGFGISTTECYTLPSLYSAPKSRNTHTCHASPSNDSWSCFKLCGVSIRDRKRRVWTASRCNDLASEKGGRHGTPPTRIPPSLPRKTTQTGAANLAYWSQFINGDKSPDGYTKHVGTDAIYAARVQAHSLTCSRLSRIVCSGSAVGWDGDDFRESDVDRECEVTSGPRPQRFCIYIMSSVSTDGGVCRKIWIFHLLSNSCRSLFSPSSDREQKLGIMAQAEVFCHALSKFLFRLCSISSLRALSSYPRSGRVLSIVTNIPQWDSRPRLRIDYHQFTPIFHNPPGKLLQPNDTCLGCSNCLQSSPLLFTRAGLLGLFRTMAPITYGCMTRSAWSSLQRGGPLDVILSTSRATLFKRCVRSRFRNPCGINVLTNFHEPRALLFSAPRGNPSYTVMFASTAATCERLALARHRTYSRFLFERTRKHALKGRTSDQDGLSAGVTWKGVNSGRYLYSTCRHGLRRLIRTMMKQIGRLFYRTRCTLLVHRDPGAEHYLSTPIVKQGRGYHRRTRLPFLLFYDQCPARGVPLLVRLVTNALSPYITMSYACQTCNRAQESVSLLPSTCAYPYRSINSDPVGAWKVGSLNTHYICKLPKVSPPRWASSQHIASTVVRSDTHSRDESINGHGRLKVAIIVCRVTARSVAEVGGYWKKRHRSPRSIFDMKNRDTWHDGGRGPTSSSDHYYPITGIPVLSTPSRRPQARLTIKSSSIWAYRDQPMLTQPCITYPVLLLQWAVASRMSAISGIRLAGLWGAANAPVQLFLYLSQCAHLGTYCVYHEMGPMYMVLPNQRRLRRFSLGGQILCYPFRTTYSRAVVRPYPDTPHGYSGNGVNTGFLRRWPGPVPCLWVKGVAHHASKLRWKTLACTALSLPALPSHPGLLKSLLKRGEVKKLEAARTVLRALQPHRTNGGYTKELGQEEEHWFRYSFGGTIGALYDRKVAVWYRSSQVIYNGPIYRLVQEPSCASPITLFSRVLLNVVSYLEITVKRHLFTPNTIPGRGLSHRKGALFFLIPPYPSSFELIRKPYRRTQPAFPGSLGDDPLLPCICRSKLRLRRITVYGSSRPVEDVGTTESRCPKTFYSLPLALCWCRSTGVGIYGYLEPDYPYYTRRAPAIPIWRHPVYRAFVQLTLAQATVPGPKPFLLLPVGTGPFIKIFGRHGFAVLAAVRYCTLCSDPIRGPDSRLSLVTESARQVLTPVEYTDLQLCSLGSIQKSKRLSRLSLTKFDELAARTNARFVRPVGYQQVKPRVIETETPYRTYRPNPPTDVDEEHKHRLLAVKRYIGFRGTLSDRPQAALIKGECKASRSGHLLEIHRGSERLDCRITLTLLKDPLGYFYGVDSQPPAVHLSYDAFSQLIKNRCFRNYKSRAFQGTNVARKSIWDRSSDPGLREPLCWTLDKRWAKYTHQPQPCQPVPTSNVFECRRGQTEVRHNALVYSPTFANFRVSADSTVLLPATGSLIVPSGRSERNPDYHAPCSLCPNLNSGLPGRIVGTPRTDKRRAVTQLRVSEASCPQRNRSPDSCALGKCPLPLDNSTSRFCGPCAHYSDLTTFLRLLFSQTSPDGRFFHQIIAVLKVGKCIRATAALNPASYLASRAAQSGNIVEGHRGPILSRSMLVKRNWRCHGSLPCNRTTGETLTILGIMYGSVGGSRILQAVVHSVARRAPQATDGFGHLLTKPFVRARTSEEDKGWVVTSIFPRRNAYDPLGKVGPTWRTPGYRMIPQADKWGIGPTNGDTANCVGGCLRVICPSRASKHHAAICLSGTSFARVGKGREEKVRHTESQAWTRFNLGNARRGGVDQILRKLTIDRGGLRGHARISTKYRPRLQRNATMAGKDTRHYLSAFKFELATRAYRSALILWELIQRSTRTLAYSTGRIELPTTVPHSSPGVVLLGVVNLRGEATQHALFSYLDSTTPYECLDIAPNSWFTSESSWPRSDAILSYRLVNDPAELLSAGPSTLSHPLCGSIGRSLTRGDRLTKDYYVVHNLSSSLTRLDRHSSATRSLRPCLWVTTENTIYLQRTCFYSDWDCMRCLSDKGGYDGNYSRVTAYHYCRPKVHDEATVLYKLKGTPIRFGPAHNHRGALALRPVETTPLRTSPEYVEHPYDEESNTGRGAARQEGLEVQLIAGQYDAWQCMDNWTVHISRLCTGVQSPPLARRVSYLGISPDIWGHSFSFRYTWPFKSSTGAIDWRHGLYSFLSTLIIGCCSRALTERSRRGPAR'
    assert(ProteinTranslation(in_) == out_), 'Test 1 FAILED'


if __name__ == '__main__':
    #test()
    print(ProteinTranslation('AUGAACGAAAGAGACCCGCCCGUUUCAGAUCUCGGCACCCUAGAACACGGUUUCCAAUGCCGUAGAUCUUAUAAGUGUACGCCUAUUUGCCUGGUCGUACGGCUCAUGCAACCACGCUCCGUCAACCGUCCGCUUCAAAUCGUUUUCGGUCCCGGCCAUGUGCACGUGGCUGCAACUCCUGUCGUGCGGCGGUUGCGGGUUAUACUUAUAGUACCUCGGUUUACAAGCUUCCUAAACCCGGUGUUGACGGUGUUAGCAGACAUGAAGUUACCCGAGGAGUUCACUAUACGCAAUGAACGUCGUUGCUCGCGUAAGAAGUCGACAUAUGCGUCACGCGGAGGUAACCAUGAUACUGGUUCGCUAUCCGGUAGCGGAUGCAUGGAAAAGCGUCUGAAUGCUGUCGCCAUGCGGCGGCUAGCGCGUAUUACCGAUCUGUGGAACGCACUUAUUACUAAAGGUACUCAGUCCAUCCGGCGCUUGAAACCGUUGAUCCGCGUGAAAAACUCUCACUCGACACCAAUACCUAUCUCGUUAGCUGACUGGAUCGCCGUAUCAUUACGUGGGCGCUCUUUCGAAAUAUGGGGAGGAGAGGUAAGGAGAGAUAAUCUUCGCUCGAGAUGUAUAGUAACAGCUGGCGCAUUUUGUUGUAGUGGCCUGCCUUGCACUUUGAGGGCCCCCGGCCUUGGCCAUGAGAACUUUAAUCCUUCUCGAGGCGAAGGCGCUAGGCACCGGCUCGGUCUACAUUUAAGCGUCUGUCCCUGUCCCGCAUCAGAUAGCUGCAGCCCCGUAAAGGACAGAUCCGCAGUCAUCUGGUCUGCGCUACAGGGACUAUGCCUGAAGGCGGGCCCACGGUUUAGUGGGGUAAUUUCAGGUUCACAGUCUUGUAAGGAUGGUCACAUUUGCGACCCAUGUGGACCACACUUGCAGCCCGGAGGAUUGACGUCGGAAGCUCCCACCUUGAACGGUAACAUCUGGCCUCCCGAACAUUGUUCAUACACCCGCCAACAUCUUAUCACGCCAUUCCUAGAACGCAUUCGUUUUACUGCAAAAUGCUCCAGUGAAUCCGAUCACGUUAUGGAGAAUCCCGCUAUGUUAGAUAGGGCGAUUACCGCGCGAGUAACGUUUAGCUCAUUGAUGCCUAGAGAGUUCUGCUUUCAAAUCAUUGUUGAACUGGCGCUCACGAGUAGCGAGUCUGAGUAUAGGCCGCAUAUUCGGAGUACUCGUAUUAGGUGCGAAGCGUAUUCGGCUCCGCCAUUUGAUCCUAGACGGCUUCUUAUACGCGCCCUCGUUCAACCAUUCUUAGUUCGCGCUGUUUGGUAUGGAGGCAGAUGUGAGCAAAGUUGUAACCCUCGACGCUUAUAUCGUGUUUCUCAUAAAUGCUUUGAUUUGAUCCGUCACGUUGGGAUCUCCUCAGAAAACCUCUGUGGCGUACAACGUAUCGUCUUAGCAGGGAGAGGUGCGAAACACCCGAAUGGUCGCAAUAAAUGCAUUCGUGAAGUAUUGGUUAUAUGGCAGCAAUGCGGAUGUCUACAUCGGUAUCGAUGGGGCCGCAUCUCCACUUGCACAGGCUGCAGAUUCGAGCCGCUGAAUUUGUUACGUGUCGUCAGGCCUAUUCAUACAGAAUUCUAUGAUAUAUGCGAUUGGUUUUGGACGGACCAGCCAUGUACGAUCCGGCUAUGGAGGGGACUAAUGUAUUCAUUGGCGCUCUUAAUCUGCAUUUCACUCCCUACAAGCCCGGCUGAACACCUCUUUCGCGGCUCUUCCACAAGCAAGCAACCCAGCAUGGGUGCUCCAGAACGCGCUAGCCAACGGAAAGCUAGCAGAACGCUUUUUGUUGAAAUGUGUCAGGCGCGGUUAUUCAUACGGAGUGUUCACAACGGCCAUGGCUUGGACUCCAAGAGCGAUAGACGUGCUAACGUUGUAUUGCAGGGGCGGGCGCGAAGUUCUAAAAAUGUUCAAUCUACCCCCCCGUAUAUCAUUGCGAUGAAUGACCCCUUCAUCUACGGUUUGCUGUAUCAUCUAUGGGGUCGGGACCACAAAGAGUCUAAAUGCACCACCCGAAAGUGUGGUGUUUCAGUGAACAGGCGUUUUUUUCCAAAUCUCACGAACUCGACGUUAUUCCCGACAGUAGUUGGAAGGGCACUUCGCAGAGGUGCAAAUUCGUUCGUCUGUGAAAUCACACCUAAACACAUAGUUCCGCCUCAGGGCCGUGCGCCUAGGCACAUAAGACACAGUAAACAAGAUAUGAAAUCAGAUAACGUCACGUCGACUAUGGCAAUCACUACUCUGUUACCAGGAAAGCAGUAUACAGCUAACUAUUUCUACAGAGCCGCUGUUUGGACAAGUCGGAAGCUGCCAUCGAGGUUUAGGAUGCAAUCAAUAGCCACGUACUCUUUGCUAGCGCUGCACAUGAAUCCUUCUGUAAAGUUACGUAAAAGAGUGCCUUGCUGUAUCGCGAGACUGAAUCCUCCGCCCCAAUUCGUGUUGGGUUCUCAACGGGGCUUCCGUCGGUAUUGGCCUAAAACUGGCCGCAGAGUGAAAACAGGACCGCAGUUGAACGCUAACACCGGUUUGAUCACUAGUGGAGAUCUACCAAGUUCAUUCUUUCCGAUUGUUUUGCUUUGGGACCGCCGGGUGCUAUAUUCUAUCAGGGGUUACAAAGAAGACGGGUCGUCCCUAGAGAGAACUCGUGCUUACACCCAAAUGGUUCGUCGAGAAAGAGUGGAUUUGCUGUACGGGUUGUAUAAGAAGUAUAUACACGCGACCACAGGACACCGCAUGAGCUCACUGAUGGUCUGCGGAGGGGUCUGUAAACGUGCAGGGGCUUGGUUGAAUCAAUACGUGUCGUUGAGGGACGAGUCGUGGCCCCGAGCUGACAUAAGGGUCCCGUUUAUGCACACUUGCAAUAAGCUCAUAUUUACUAAUCCGAGCUGUCUCAUUCCAAUCCGCCAAGAUGGGAUUCAUACAAGUCUAAUAUUUAUGGGUGGAGUACUCUUCCGGCCGCGCCCGAUAGCUACAGGGAGUCGUGCCCUUCCUAGCAAAGCGCUUGGUUGUACAAUCACGGGACCCACGGGACGAAUGUGCUGGAUGUCCCGCUUUCCGAUUCUCAAGUCAAAGGUUCUCUCGGAGAACCCUUACCGAAACUUUUUAACGAAAUUCUGGACGGCUGAAUCACAGUACGGAUAUAAUGUGGGAUUCUGGAUGAAGCGCGUAGUGAGGGCUCCAGAGUCAAUAAGGGUCAGAGCAGAAAUACUAAUGCGGUACCAGUUUAGCCGAUCAGUUAUUCACGCCGGUCCGGGAAAGCCAACGCCAUUUCCGAUAUCUAGCGAACACUUGCGUAGCCUCAGCAACAAACAAAGGAAUCAGUUUCCUACCUCGCUCGUAGUCGGCCAAUCAGGACCCUAUUUCAAAUUAUGUCAACGAUCUGCCCUCUGUUUAAAUAAUGAUGCUAUAUUACCAGAAGCUAUAAUCAGUCUGGGAGCGCCAUCGUGGGUAGUAAUCGCGGGCUUUGGGUUCGCUCGAGGUUUUAGUCAGACUAACCGGAUAAUUCUGAUGACUGGCUCUCAGCGAAAGCCAUAUUUAUCCCGGAACCGGUUGCUGCAUAGACACCUAGCCUCGAGAUUAGGGGCGUGUCUCGACUACUACCCAGCUACGACUCUGGUUGCUAAACUUUAUUGGGGGGGAAUGAAUGUGCGCUCUGGGUCGCAGUGUCGUAGCGCCAGUGCUGUUGACCGUACCAAUCCGGGGAUGUGGCAAAACUCAUUCGAAAAUAAGGGGGAGCAGAGCGCCCGAAGUCGUGUUCUACACGUCGAGGUUUUUUCCGAGCUCGUUGGCUACAGCAGGUCGGGAUUUCGGGAUUCCAAAUUGCCGGCGAGGAGUCGACUAUGCUCUGGUAUAACACUUGCACCGUUACGUCUCGUUGAUUCCUGCGGGAUAAAGAAGAGCGGCGGGACCGCGGGAGUGACUGCAUUACCGCAUAAUACGAGGCGCGUAUCUGAUAUCGAGCUGUUAUCUGGCUCCUCUGUGAGCAGCUUUCAGGCGUUGAGCAGGUUCCGCGCAAAAAUGGUAUUUACUGACUUUGGAACUCAAGGCGUAGAAAGAUCCUCAAGUGGUCCGGACUUUGUCAUGCAUCACUGCCGUGACUUACGACCGGGCAGCCGUAACCGCAUCCUAUUAGGUAGUCAGAUUACAUCAUCUGGAACGUCCAGCGAGAUGGGGAAUUUGGGGCGGCUGUCACGAUCUUUGGCCAGUCCGCAGGAACCUGCAUACGGAGGAGGCGAAACCUAUUUAACCACGCAUACAGACUCUGGCCGGGAUCAACUAAGGGCCUACUUUGUUAUUAUCAAUAAGACCAACUGCUGUAACAAGUGGUUACUUCACAGAUUGCGUAACACAAGGUCCAACCACCCUGGUUAUGAGUCUGGCAAAAAUCAUUCCGUCUGUGCUGCACGCAACAAUUUUUUGUUUAACAAAAGCUCCACUCUGACGCUACUCGAAACUAUAACCGCGAGUAGUCGCGAUUCAGUUCCGGCGGAUCUACGCCUUGCCUUCUCAUCGGUCCCUAAUGCGACUGAUUCUCAACUCAAUGUCCUUGACCUUGUAUCUACGUGUGCCCAACCAUCAUGUGAUUCGCAUCACGGCCUUGUUUUCCGGUUGGCAAAGUCAUCACCAUCGGUAUCACGGAAUGCAGAAACCCAUGUGAUCUGCCACACGAUUGAUAUACGCUUCGCCUACGCGGCAUGCGUUCACCGAUCCUGGGAUAACUUAGGAACGUCACUCUCAAUAGCCGCCAAUUGGGAGGUGUGUUGCAGCUGCGGGGAUCCUCUACUCUUUUUUAUGUUCGCCGGCAUACAGAGACCUGAUAAAUACAAGUCUUAUUGGAAGUACUUCACAGGACAGUCGCAUGCGCUUUUCUCACCGUUUGCCCCGAGAGAGAGGCAGAAUUUAUCAACCGUAGCGCGAAAACUGAUCAACACUGCUCGAUUCGGUCAUCUGUAUGAACGGGACUACAUACCAAUGAAAAGUGGAUGCGAAAGGUUAGUAUGGAACGAGAUAUGUAUGUGCGUUGCCUGUAUCGUCCCUCGUCGUUGGCAACAGUCUGAAACGAAUCUUACAAGCCAGUGUUCGGCCAUAGGCAUUAGGUAUUCAGUACCACUGUCCGCCCGUAUCAGACCAGAAUACAUCUGCACCGGUUCAGGGGGUGGGAGGAUGUGCAAUGAUGUCAGAGGGUACCACCUAGCGAAAGGGCGAGCUAGUCACAAAUUUAUUAACCGUGAUACCCGCCUCUUACCCACCUUGAAAUCACCGUUAACGCUGAGAAACGAAGGAGGCCUUUUGGGGUUGAAACAUCAUGGACUGUGUGACUCAAAGGGCGUUUUGCUGGCAGGAGCGUCAAUGCCGCAGUUGAGCAACAGAAAUAGCUGCUGCACCCCAAUGGGUCGAGCAACCGCGGUAAGCGGAGUUCUCUUGCCCCAUGAGCUCAGGGGCAAGGUACGUUUGUACAUCUGGGGACCACGUCCGUAUUCUGGCAGGCCAUCCGAUCCCUCCGUUCUUGGUGACACACCGGCAAGUCGGCAUCAAGUGACGGGAUACUUGAAUCUAGGAACAUGCUCCCAGGCGGAUCGUAACCAACUAGAUGUCAAAGGACCUACCUACUCCAUCAGACACCGGUUACUCGCGGUCAAUAACGACCGACCCCAGGUCACGCGGUUCGCGAUAACUGCUCUGAUCUCACUUGUGCAACCGCGCUCUGCUCCUGUUCCCGCAAGGAGUCUGAUAGACGAACGCCACCUUAGCACCAUCCACCCCUCUGACCACGACGUGACCACACACUGGGAUCUCCAUGCGGGUAUCUUAACUUUCAGAGGUACGAGGAAUUACUUUUCUGUUUCGGUCCAUCAAAUACUGAAGCGGCUAAUGGAAGCCGGUAAUACGAAAUCAUAUUGUACAUCGCCGACACCUGCACGUGACAGAUACGGAGUCUACCUACGUAAUCUAAGGGACCCGGUCGAAGGUCCCGGGGACUGGGUAGUGUCCCGGGGGUCGGGGAAUUGUGCCUCUCGACACAAUUUAGUUCUCCGUAGCGAACACUCCAUUUUGUCAGUUGGGAACACAAGAAGCAUCAAUCCGGUGAUGCCAUCCGGUUCAGCGGGUAUAUCACUGGCUUUGGCACUACUUCGCCGCCCUACGAAUUGCGUACAGUGGUCCCAUCGAUGUUUUAGGUUCACGGAAGAACUACCGAGUGCCGCGUUUUCUCAUCAAUUGAGGGUGCGGGAGCUACGAUGGUUGCUGAACAAGCGCCUACGAAGUUUACGUUGGAUUUUGACAGACUGUUUUAAAGCUGGCGGAAACAGGGAGUGCCGCGUCGACGCUUCCGCUUCAUUACGCCUCCGCCGCCCUGAGAAAACCGUAAAGAACCUACACCCCUGCACGCAGUUAAACACGGCCCCAUUUAUGAGAAGAGGACGUUCGAUGAAAGAUCGUUCUCUUUUAGACUCUUUGGAGCCGACAUCCUUGCUUAAUAAGACAGUCACGAGUAUUAGAACGCCAACCUUUUACUACCUAAUUCAUUCUAAACCCGGACUUCCAGCGAUUCAACGAAGUAAUGAGUGUCAUGUUCGCUCCGGGGCAUAUAUUCCGGCGCCUAGUCGAAAACUGUGUCGAUCACGUUCAAUGCACGUAAAGCCAAUUGGUGUCUUUUUCCACCGUCGGGUACGAGGGCUGUCCAAAGACUUUUGCCGCCAAGUGCUAGGCCCAUACCAGCUCAAGUUCGUGGGAUUGAGACGUUGCCAUUGCGAGGGGCCCUAUGGCCUCGGAGAGGGAGAGCCUCCUUGGACCAUCUUUGGUGGCUUUGUUUCUUAUAGUCAUCCUCGAGUGUAUCUGGGGAACAGUGAGAAUAUCGUUCCAAGUCAUAGCGAUGCUGUGUCCUUUCGCGUAGGCAGGUGUGAUGUGACUUGGGGAAGAAUCACAAGUCCUGUACCAAAGGUAAAGUGUUUCUUGGAAAAUCGAUGUUCGUCCUAUCAUGGUGGCGGCAAUCUUGUGGUCAGCGCGGUUAGUCACACUACAUUGCCUAUAGCAAGGUGUACCAGUGUUGUUACCCGCUUAGCAGGCCAAGGUCCGCAAUACAUACGACGUCUUGUCGAGUUUAAUCCAAUUGAGAUGCAACCCAAUUAUGUGGAGAUGGGGGAGGGACCAGACUCAAGACAAAUUUUAUUCCAGAUCCGGCUGUUAGGCUCUAGACGACCAGUUCCUACCCAGACCUACUCCACCACCUGGUGGCGAGCGUGGAUUCAAAUUAUCUGCGCCCUCUACAUCCUCGCCACCAGGAGAGUAACCGUAGCAUUACACGUACCAAGCCCUAAACUCUCCGUAUCAUACGAUCCUGUGAUACUACCAACCAUGGCUACAUCAACUGAAAUAUUUAUCCGGUGUGACCCGGGCGCCGUAGGGGACACUGAGUCUGGGCGGCCGAAUCCAGGUGUUCAAUAUUACCAGAGAGGGAAUCGCACCCCCCCAAUUGCGUGGGGCAAGGCUAGUAUCAUACAAACCCGCCAUGCGCAGCCUCAAAGGAAAAGCGCGAACUUAGUGGGCGUAAACGACUUUUUACAUAUCAUUGCCGGUCACCGCACUAACGAAAUUCUGGUGUCACAACCGCCCCUUCGCGACGUUGUCGGAAGUUUGAAAAAUGCGCCUCAGAUGACUUGUAAGACUAUGGCAAAUGCCGCCUACUACCGUUCUUGUCGACGGUUGAUGCAACAACCAAUCAGCGUCAAGCCUUUUUGGCUAAUUGAGUCAGCGCACACGUCAAUCUGGCCCGCUGGAGACCCGUGGCAGUUAGUUCAACUGCAACCGACUCCAGCUGAGUGUCGCGCAGGAUAUACGUCUUUGUGGCGGGUACGAUGCAACGUUUGCGGCGUCCCGGACGAGCUGGCGCAUCUUCCCCAACAAUCAGGGAAGGUCUCCAGGGAGGGCUGGUGCGGUUGGCCGUUAAUGUCCCCUAGCAAAAAGCGGUAUGAGCAGAUUCUCACCGUGAGGAUUUGGGCAUGGGCCAAUCCGCCACUAGCGCGCGAUCCGAGGCUCGCGAACCAUGUUAUUACGGCUCUGGUGUCUCAUGUAGAGUUGCGACGGUCUGAGCGUAUGAAGUACGUUUGCACCACACGCAAUAUCAUCAGCAGACCGCCAGCACAACCGAGCUCAGGGGGUGCCUUAAAUCCGCUUUUGGCAGAUAAAAAAAUAGUCUACGAGUAUGAGCAUGAAGCGACUCUUAGGUCAUCGAAGCGGAUUUUGCGACAAAGUAAUCGCGUCCGUGCCGCAAUUUUACCGAUUUAUCAUACCGUUGCUAGUACUCGUGUCCCACAAGGACUUGGGGUCUACGAGACUCGAGCCGUGCCUGGUCAGCGGAUACGUGCCCCGCGGCAAGAAACGGUGAGGUCUAUUGUAACUUUCGCCGGGCUCUCCUGCGAAACAGUCGUUCCAAAAUUCCUCCAUAACGAGAGACCUCGUUUAGCUUGCAAGCUCUCCCUCACACCCAAUCUGUACACCAGCAGUACACUGUCUGCAGUGUCUCGCUCACACACACUGAUGGUUAGCGCCGCUUGGGCUCCCAGAGAACGGGCUACCUGUUGCUCGCGCGUCCGGUUGUACUGUUUUUUGUUGUCAAAAUCGCGCGGAAAUCGGAUGUUUUCAAGAUACUAUGUAUUGCGACACCUGGGAUGCCUCUACCACUACGCGCGUGCUAGAGCUCGUAAGAUGACCUUCUCCAAGGCCCUAGAUCCUAAGUGCAGACCCUCAAUUGUGAGAGCGUCACCUCUCGCGCAUUCAGAGGUGAGAAAAAUGAGCGACAGUUGCCAUCGCAGAACGAGUGCGCAUACGGUAUAUGUAUUCUGUCGCGGUUACUUAGGAUUACCCACGUAUCUCAGACGAUGUCACCCUAGUUCCGCCUCGCUAAUUACACAAAUGGCAAAAGAUAGCCCCCAUGAUCUUGGUCUUUUUCGACAACGGUCUCCCCCCUCUAUAUUCCCUCAUGAUUACCUACGACUAUCAGGUCUGACGAUGGGUACCGCGGGUCCACCUGGACAGCCUGCGUCCAAGCGACAGGGUCAACGUUGUGGGUCGGCGAAUGUAAUCGCCGGCCGAAUCACGGAUGGCGUGUUGCCCCAGCAGCCUGUCCUAGGGACUCUAGCUCAAGCCACUCUGCAACAACCUACGACUAGUGCAAACCUUGUAGUAUCGCGGACCGGAGUGGCCGUGCCACUGACCAUUGCCUCGUAUCUGUACGCGUAUUCGUACGGGAGCCGCCCAAUACGCCUAUAUGACUAUCGAUUGCAAUCAUGGGUUGGCUAUGAGGAGAUGCAUCAAACGUGUUCCAUAUGGGUUUUCGCAAGUAACGGGGAUGACGCGCGGGGCACUCAACUCGGUAGGGCCCUAAAUUGGGUGCUACCCCCGGUUCAAUUUCGGCUGCACAUCUGGAAAGAUCUUAAAUCUUUACUAACAAGGCGGCGGGUGAUGACAGAAUGGUCAGGAACCCAUAAGCGGUAUUGGGACGAACAGAUAUUCCUCCACCACAAACCCCGUAUUGUUAUAAAGAGAUGCUUUUUUGAGAGACAUUCAGCGAAUAAUUUUGGCCUUACAACAAGUAGAGAGCAACGGGUUUCGUUAGUGGUAAAAUUACGAUUAAGUGCGCGUUUCAUGGGAGUCGUGGUCCCAUGCACACAUCCUUUGGGUCGAAUAUCCUGGGCAUUCCAGUACCUAAUAGUGCGCUCGGGUGGAAGGACAGUACUUUUUCUUGACAGAUAA'))


