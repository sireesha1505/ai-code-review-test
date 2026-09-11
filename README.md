# AI Code Review Test

A small repository used to test an AI-powered GitHub code review system.

## Project Structure

- `add.py` - addition utility
- `mul.py` - multiplication utility

## Coding Guidelines

- Use type hints for function parameters and return values.
- Keep functions focused on one responsibility.
- Avoid unnecessary code duplication.
- Validate inputs where appropriate.
- Add unit tests for new business logic.
- Test important edge cases and error paths.
- Avoid inefficient algorithms when simpler approaches exist.
- Never expose secrets or credentials in source code.

## Testing

Run tests with:

```bash
pytest