# Deep Learning From Scratch 4
본 저장소는 Deep Learning From Scratch 4를 기반으로 강화학습을 공부하기 위해서 만들어졌다.
기본적으로 본 책에 작성된 코드 위주로 구성되었으며, 추가적으로 각 챕터에 대한 요약본을 각 폴더의 README.md에 작성하였다.

# Summary
| Chapter | Notion | Python |
|---------|--------|--------|
| 1장 밴디트 문제 | [![Open In Notion](https://img.shields.io/badge/Open%20in-Notion-000000?logo=notion)](https://honorable-noodle-1d0.notion.site/Chapter-1-1ec08f682c5a80f68354fa103ea33a7c?pvs=4) | [![Python](https://img.shields.io/badge/Open%20in-Python-3776AB?&logo=python&logoColor=ffdd54)](https://github.com/MonoHaru/deep-learning-from-scratch-4/tree/main/ch01)

# Chapter 1 - 밴디트 문제

# 1.6 정리

- 강화 학습
    - 환경과 에이전트의 상호작용이 이루어짐
    - 에이전트는 자신의 행동에 대해 보상을 얻고 보상의 총합을 극대화하는 행동 패턴을 익히는 것을 목표로 함
- 벤디트 문제를 위한 알고리즘
    - 여러 선택지 중에서 최선의 선택을 고르는 문제에 적용 가능
- ‘활용’과 ‘탐색’의 균형
    - $\epsilon$-탐욕 정책
        - 지금까지 얻은 경험을 ‘활용’
        - 동시에 탐욕스럽지 않은 행동을 ‘탐색’
    - UCB(Upper Confidence Bound)
    - 그레이디언트 벤디트 알고리즘
- 평균
    - 표본 평균
        - 균일한 가중치를 사용
    - 지수 이동 평균
        - 새로 얻은 데이터일수록 큰 가중치를 부여
    - 두 평균을 기반으로 ‘행동 가치의 추정치’를 계산 가능
    - 보통 정상 문제에서 표본 평균, 비정상 문제에서 지수 이동 평균을 사용