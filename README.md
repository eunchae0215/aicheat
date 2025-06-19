docs.txt 만 사용 ㄱㄱ



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



1단계: 문서 임베딩 및 저장
TextSplitter로 문서 분할

Chroma에 임베딩된 벡터 저장

2단계: RAG 체인 구성
ConversationalRetrievalChain.from_llm()으로 생성

3단계: Agent 체인 구성
initialize_agent()로 구성

retriever_tool을 Agent에 연결

4단계: 질문에 대해 두 체인의 응답 비교
예시 질문:

"What are the key components of LangChain?"

"How is context handled differently in RAG versus chat agents?"

5단계: 응답 비교 및 분석 출력
정확성, 표현 방식, 길이/품질 비교

RAG와 Agent가 각각 유리한 상황 분석

설명은 최소 600자 이상

| 항목             | RAG 체인                           | Agent 체인                                    |
| -------------- | -------------------------------- | ------------------------------------------- |
| **응답 정확성**     | 제공된 context 기반 응답, 제한된 reasoning | Tool 기반 확장된 reasoning 가능, context 외부도 접근 가능 |
| **응답 방식**      | 직접 응답 (retriever → LLM)          | 관찰값 기반 reasoning (Tool 사용 후 응답)             |
| **응답 길이 및 품질** | 간결하고 명확함                         | 길고 자세하며 reasoning 과정 노출 가능                  |
| **유리한 상황**     | 문서 기반 QA, 정적 context             | 복합 reasoning, 외부 연산, 조건 분기 처리 등             |

결과 요약 및 600자 이상 분석 설명 (파일에도 포함)
RAG 체인은 정적인 문서 기반 질의응답에 매우 효율적이며, 관련 context를 LLM에 직접 주입하여 응답의 일관성과 정확도를 보장한다. 반면, Agent 체인은 tool을 기반으로 행동을 선택하고, 외부 정보를 동적으로 수집하거나 계산을 수행할 수 있어 유연한 reasoning과 복합 질의 해결에 적합하다. 예를 들어, "LangChain의 구성요소는?"이라는 질문에 대해 RAG는 docs.txt의 핵심 내용만 요약하여 직접 응답하고, Agent는 document_retriever tool을 호출해 그 내용을 분석하고 reasoning까지 포함해 더 풍부한 응답을 생성한다. RAG는 짧고 정확한 답변이 요구되는 경우 유리하고, Agent는 행동 기반 응답이 필요한 과업에 적합하다.


