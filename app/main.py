import psutil
import json
import argparse
from datetime import datetime

def collect_system_metrics(verbose=False):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_usage_percent": cpu,
        "memory_usage_percent": memory.percent,
        "disk_usage_percent": disk.percent
    }

    if verbose:
        print("Metrics collected successfully")

    return report

def main():
    parser = argparse.ArgumentParser(description="System Health Reporter")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    report = collect_system_metrics(args.verbose)

    with open("system_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
