# testproj

Python TDD 프로젝트.

## 프로젝트 구조

```
testproj/
├── src/          # 프로덕션 코드
│   └── __init__.py
├── tests/        # 테스트 코드
│   ├── __init__.py
│   └── test_example.py
├── pyproject.toml
├── CLAUDE.md
└── .gitignore
```

## 환경 설정

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
# source .venv/bin/activate    # macOS/Linux

# 개발 의존성 설치
pip install -e ".[dev]"
```

## 테스트 실행

```bash
# 전체 테스트
pytest

# 커버리지 포함
pytest --cov=src

# 특정 파일만
pytest tests/test_example.py

# 특정 테스트 함수만
pytest tests/test_example.py::test_placeholder
```

## TDD 워크플로우

1. **Red** - 실패하는 테스트 먼저 작성 (`tests/test_*.py`)
2. **Green** - 테스트를 통과하는 최소한의 코드 작성 (`src/`)
3. **Refactor** - 테스트를 유지하며 코드 개선

## 컨벤션

- 테스트 파일: `tests/test_<모듈명>.py`
- 테스트 함수: `test_<기능>_<시나리오>()` (예: `test_add_negative_numbers`)
- `src/` 모듈은 `from src.모듈명 import ...` 형태로 import
- 각 테스트는 독립적으로 실행 가능해야 함 (공유 상태 금지)

## 의존성 추가

`pyproject.toml`의 해당 섹션에 추가:
- 프로덕션 의존성: `[project] dependencies`
- 개발 전용 의존성: `[project.optional-dependencies] dev`
