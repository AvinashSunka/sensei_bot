# Sensei

An educational Discord bot that powers CS communities with daily LeetCode challenges and data-driven peer mentorship.

## Planned Features

* **Automated Daily Challenges:** Posts two daily LeetCode problems directly to the server with scheduled reminders to maintain competitive momentum.
* **Weakness-Based Recommendations:** Analyzes individual performance to deliver targeted problem recommendations, helping users systematically bridge knowledge gaps.
* **Personalized Analytics:** Tracks detailed statistics for every user, enabling comprehensive personal progress analysis over time.
* **Peer Learning & Mentorship:** Generates smart peer suggestions, connecting users with similar skill levels for collaborative problem-solving.
* **Curated Resources:** Automatically suggests relevant learning materials and study guides based on current topics or recently failed concepts.
* **Discussion Scheduling:** Features a dedicated room-scheduling system for live classes, mentorship syncs, and group study sessions.

---

## System Architecture

Sensei is built for high scalability and maintainability, leveraging a microservices architecture:

* **Domain-Driven Design (DDD):** The codebase strictly separates Discord API interactions (Controllers/Cogs) from the underlying business logic (Service Layer).
* **Microservices Ecosystem:** The platform consists of independent services communicating via HTTP/REST. Current microservices include the main Discord Bot and the `leetcode_wrapper` (which handles LeetCode API interactions).
* **Asynchronous Design:** Developed using modern Python `async` and `await` paradigms via `discord.py` (v2.0+) to ensure non-blocking concurrent operations.
* **Test-Driven Development (TDD):** Comprehensive unit and integration testing workflows are enforced via `pytest` and Docker before deployment.

---

## Development Guidelines

We welcome contributions! To maintain the structural integrity of the project, please follow these setup and architectural guidelines.

### Prerequisites

The entire development environment is containerized. You only need Docker and Docker Compose installed on your system.

* **Linux (Arch):** `sudo pacman -S docker docker-compose`
* **Ubuntu/Debian:** `sudo apt install docker.io docker-compose-v2`
* **macOS/Windows:** Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### Local Setup & Execution

1. **Start the Microservices:**
Build the images and spin up the bot, wrapper, and databases. The `compose.yaml` is configured to run tests automatically before starting the bot.
```bash
docker compose up --build

```


2. **Force a Clean Rebuild (Optional):**
If you change dependencies in `requirements.txt`, clear the Docker cache:
```bash
docker compose build --no-cache
docker compose up

```



### Testing Workflow

Sensei enforces a strict TDD pipeline. The bot container will gracefully abort deployment if any tests fail.

1. **Viewing Test Results:**
When the tests finish, Docker automatically mounts a styled HTML report back to your local machine.
```bash
# Copy the report to your root directory for easy viewing
docker compose cp discord_bot_tests:/app/report.html ./report.html

```


Open `report.html` in any web browser to view the detailed pytest execution logs.
2. **Debugging Failing Tests:**
To view the raw terminal output of the test container:
```bash
docker compose logs discord_bot_tests

```

3. **Manual Testing**
To manually run the tests:
```bash
python -m pytest -v --html=report.html --self-contained-html --css=report_style.css
```



### Contribution Rules

* **Respect the DDD Architecture:** Never write business logic, database queries, or string formatting inside a `discord.py` Cog. Cogs should only parse the user's input, pass it to a Service class in the `core` directory, and return the response.
* **Write Tests First:** Any new feature added to the Service layer must have a corresponding pure-Python unit test in the `tests/` directory.


---

## 🔗 Quick Links

* **Add Sensei to your server:** [Invite Link](https://discord.com/oauth2/authorize?client_id=1561535149030645850)
* **discord.py Documentation:** [Click here](https://discordpy.readthedocs.io/en/latest/index.html)
* **pytest Documentation:** [Click here](https://docs.pytest.org/en/stable/index.html)