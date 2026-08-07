# observability-lab

A hands-on lab for the Obsernetics blog series on **Observability** with the Grafana
**LGTM** stack (Loki, Grafana, Tempo, Mimir) plus **Pyroscope**, running on a single-node
**k0s** Kubernetes cluster and deployed with **Argo CD** (GitOps).

آزمایشگاه عملی مجموعه‌ی وبلاگ Obsernetics درباره‌ی Observability با استک LGTM و Pyroscope
روی Kubernetes (k0s) و استقرار با GitOps (Argo CD).

## Layout

| Path | Purpose |
|------|---------|
| `bootstrap/` | Argo CD install + root app-of-apps |
| `apps/` | Argo CD Application manifests |
| `django-app/` | Sample instrumented Django app (source, Dockerfile, manifests) |
| `platform/` | LGTM stack + Pyroscope + Alloy manifests |
| `dashboards/` | Grafana dashboards as code (JSON in ConfigMaps) |

## Series

1. k0s prerequisite
2. Django on k0s via GitOps (Argo CD)
3. Metrics (Mimir)
4. Logs (Loki)
5. Traces (Tempo)
6. Continuous profiling (Pyroscope)

Blog: https://obsernetics.com/blog/
