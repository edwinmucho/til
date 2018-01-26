from konlpy.tag import Kkma, Twitter
from konlpy.utils import pprint

# kkma = Kkma()
# pprint(kkma.sentences("네 안녕하세요. 반갑습니다."))
# pprint(kkma.nouns("질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요."))
# pprint(kkma.pos("오류보고는 실행환경, 에러메세지와함께설명을최대한상세히!^^"))

tw = Twitter()
pprint(tw.nouns("질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요."))
pprint(tw.pos("오류보고는 실행환경, 에러메세지와함께설명을최대한상세히!^^"))
