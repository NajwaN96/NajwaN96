# Najwa Alshahrani

### Cloud & DevOps Engineering · Automation · Reliability

I build engineering projects around cloud infrastructure, Kubernetes, observability, and controlled incident recovery. I am expanding toward **AI Engineering**, with an interest in deploying, evaluating, and operating reliable AI applications.

[Portfolio](https://najwa-alshahrani-portfolio.e-newint1.chatgpt.site/) · [LinkedIn](https://www.linkedin.com/in/najwaalshahrani)

## Selected engineering projects

### [KubeMedic](https://github.com/NajwaN96/kubemedic)
A Kubernetes reliability lab for investigating workload failures, collecting evidence, tracking recovery, and proposing human-approved remediation.

- **Engineering:** Python, Kubernetes operations, observability, and controlled recovery.
- **AI-assisted investigation:** rule-based diagnosis with an optional AI explanation of collected evidence; AI does not execute Kubernetes operations.
- **Scope:** an engineering lab; the AWS infrastructure design is not provisioned.
- **Explore the evidence:** [AI provider implementation](https://github.com/NajwaN96/kubemedic/blob/main/kubemedic/app/ai/openai_analyzer.py), [sanitization tests](https://github.com/NajwaN96/kubemedic/blob/main/kubemedic/tests/test_ai_sanitize.py), and [lessons learned](https://github.com/NajwaN96/kubemedic/blob/main/docs/lessons-learned.md). The optional AI integration has not been exercised with a live provider in the documented lab.

### [OpsPilot](https://github.com/NajwaN96/opspilot)
A reliability control plane connecting service degradation, operational evidence, constrained rollback proposals, human approval, and recovery checks.

- **Engineering:** Go, Next.js, PostgreSQL, Prometheus, OpenTelemetry, Kubernetes, and GitHub Actions.
- **Explore the evidence:** [architecture](https://github.com/NajwaN96/opspilot/blob/main/docs/architecture/overview.md), [five-minute walkthrough](https://github.com/NajwaN96/opspilot/blob/main/docs/RECRUITER-DEMO.md), and [AI/execution boundary](https://github.com/NajwaN96/opspilot/blob/main/docs/adr/0016-ai-recommendation-vs-execution.md).
- **Scope:** the interactive workflow runs locally; the [public AWS portfolio](https://jcqljkrf25oijz4cryqw7c76lq0wmzhi.lambda-url.us-east-1.on.aws/) presents sanitized, read-only samples. EKS infrastructure is plan-only.

### [Thmanyah SRE Challenge](https://github.com/NajwaN96/thmanyah-sre-challenge)
A microservices infrastructure challenge exploring containerization, Kubernetes deployment, monitoring, and failure scenarios across Node.js, Go, and Python services.

- **Engineering:** service integration, PostgreSQL, observability, and reliability exercises.
- **Scope:** a challenge project demonstrating implementation and architectural decisions. See the [architecture diagram](https://github.com/NajwaN96/thmanyah-sre-challenge/blob/main/architecture.png) and [failure scenarios](https://github.com/NajwaN96/thmanyah-sre-challenge/blob/main/scenarios.md). The README explains the current reproduction limitations.

## Growing into AI Engineering

My systems projects provide a foundation in deployment, monitoring, auditability, and human oversight. I want to apply this foundation to AI applications while developing deeper skills in **model evaluation, LLM applications, retrieval-augmented generation, and MLOps**.

Explore the repositories above for source code, architecture, setup instructions, and project limitations.
