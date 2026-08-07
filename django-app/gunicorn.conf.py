bind = "0.0.0.0:8000"
workers = 2
accesslog = "-"
errorlog = "-"

def post_fork(server, worker):
    import os
    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.instrumentation.django import DjangoInstrumentor

    endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "alloy.observability.svc:4317")
    service = os.environ.get("OTEL_SERVICE_NAME", "guestbook")
    provider = TracerProvider(resource=Resource.create({"service.name": service}))
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint, insecure=True)))
    trace.set_tracer_provider(provider)
    DjangoInstrumentor().instrument()
