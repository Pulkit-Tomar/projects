# 1. SETS: Best choice for high-speed lookups of malicious IP indicators
THREAT_INTEL_IPS = {"185.220.101.5", "45.144.225.10", "89.248.165.4"}


# 2. FUNCTIONS: Reusable blocks to keep the script structured
def read_log_file(file_path):
    """Reads lines from a log file using native file handling."""
    try:
        # FILES: Opening and safely reading data line-by-line
        with open(file_path, "r") as file:
            # LISTS: Storing processed lines from the file
            log_lines = [line.strip() for line in file.readlines()]
        return log_lines
    except FileNotFoundError:
        print(f"[!] Error: The file '{file_path}' was not found.")
        return []


def analyze_logs(log_lines):
    """Parses log entries to flag known threats and track failed logins."""
    # DICTIONARIES: Perfect for pairing unique items (IPs) with changing values (counts)
    failed_login_counts = {}
    flagged_threats = []

    for line in log_lines:
        if not line:
            continue

        # Splitting raw string data into workable parts
        parts = line.split(", ")
        if len(parts) < 3:
            continue

        timestamp = parts[0]
        ip_address = parts[1]
        status = parts[2]

        # Checking against our threat intelligence SET
        if ip_address in THREAT_INTEL_IPS:
            flagged_threats.append(
                f"[ALERT] Known Malicious IP detected: {ip_address} acting as '{status}' at {timestamp}"
            )

        # Counting occurrences using a DICTIONARY
        if status == "LOGIN_FAILED":
            if ip_address in failed_login_counts:
                failed_login_counts[ip_address] += 1
            else:
                failed_login_counts[ip_address] = 1

    return failed_login_counts, flagged_threats


def generate_security_report(failed_logins, threats, report_path):
    """Writes the security findings out to a new text document."""
    with open(report_path, "w") as report:
        report.write("=========================================\n")
        report.write("        CYBERSECURITY ALERT REPORT       \n")
        report.write("=========================================\n\n")

        report.write("--- Threat Intel Matches ---\n")
        if not threats:
            report.write("No known malicious IPs detected.\n")
        for threat in threats:
            report.write(f"{threat}\n")

        report.write("\n--- Suspected Brute Force (Failed Logins) ---\n")
        brute_force_detected = False

        # Iterating through dictionary data
        for ip, count in failed_logins.items():
            if count >= 3:
                report.write(
                    f"[CRITICAL] {ip} flagged for potential brute force ({count} failed attempts)\n"
                )
                brute_force_detected = True
            else:
                report.write(f"{ip}: {count} failed attempt(s)\n")

        if not brute_force_detected:
            report.write("No brute-force thresholds breached.\n")

    print(f"[+] Security report successfully generated at: {report_path}")


# Execution Flow
input_logs = "server_logs.txt"
output_report = "security_report.txt"

print("[*] Starting Native Log Analysis...")

# Call the functions sequentially
raw_logs = read_log_file(input_logs)

if raw_logs:
    failed_attempts, malicious_activity = analyze_logs(raw_logs)
    generate_security_report(failed_attempts, malicious_activity, output_report)
