txt 파일 일단 두 개 올려서 해 보는 게 나을 듯


1단계: 문서 임베딩 및 벡터 저장
textsplitter로 문서를 분할하고 크로마에 저정
2단계: RAG 기반 체인 구성
conversationalRetrievalChain.from_llm() 을 이용하여 기본 RAG  QA 구성
3단계: Agent 체인 구성
initialize_agent 사용
tool로 retriever_tool 을 등록
Agent는 다음과 같은 동작 흐름을 갖도록 설정: 사용자 질문 해석, 어떤 tool을 사용ㅇ할지 판단, 선택한 tool을 실행하여 관찰값을 수집, 최종 응답을 구성


각 질문에 대해 두 체인의 응답을 나란히 제시하고 응답의 정확성을 설명하고 응답 방식의 차이를 설명해야 함
ex. what are the key components of  langchain? (정의+구조)
ex. how is context handled differently in rag verus  chat agents? (비교+분석)



+ 두 체인의 구조 요약 (도식 또는 표 가능)
+ 응답 내용의 비교 1정확성 (틀린 정ㅇ보 여부) 2표현 방식(직접응답 vs reasoning) 3응답 길이와 품질
+ 어떤 경우에는 RAG가 더 나은지, 어떤 경우는 Agent가 유리한지 분석

(제출문이  rag_vs_agent.py 또는 .ipynb로 나와야 함)
(설명이 600자 이상 되어야 함)
