# Copyright (c) 2026, Omnexa and contributors
# License: MIT
"""omnexa_eng_platform_integrations gap register — 48 items vs global platform leader."""

from __future__ import annotations
import os
import frappe
from frappe.utils import get_bench_path

GLOBAL_LEADER_TARGET = 4.85
GAPS_TOTAL = 48
APP = "omnexa_eng_platform_integrations"

GAP_DEFINITIONS: list[dict] = [
	{"id": "EP-001", "domain": "integration", "title": "Global benchmark module", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-002", "domain": "integration", "title": "Gap register", "wave": 1, "detect": "module:epi_gap_register"},
	{"id": "EP-003", "domain": "integration", "title": "App hooks registered", "wave": 1, "detect": "file:hooks.py"},
	{"id": "EP-004", "domain": "integration", "title": "Assessment export", "wave": 1, "detect": "module:epi_assessment"},
	{"id": "EP-005", "domain": "portfolio", "title": "Consulting bridge", "wave": 1, "detect": "file:consulting_bridge.py"},
	{"id": "EP-006", "domain": "integration", "title": "Engineering consulting app", "wave": 1, "detect": "module:omnexa_engineering_consulting.eng_gap_register"},
	{"id": "EP-027", "domain": "reporting", "title": "Platform API reporting surface", "wave": 1, "detect": "file:api.py"},
	{"id": "EP-008", "domain": "analytics", "title": "Sector analytics API", "wave": 2, "detect": "api:omnexa_eng_platform_integrations.epi_global_extensions.compute_sector_analytics"},
	{"id": "EP-009", "domain": "analytics", "title": "Demand forecast API", "wave": 2, "detect": "api:omnexa_eng_platform_integrations.epi_global_extensions.forecast_demand_pipeline"},
	{"id": "EP-010", "domain": "analytics", "title": "Executive dashboard API", "wave": 2, "detect": "api:omnexa_eng_platform_integrations.vertical_dashboard_api.get_vertical_dashboard"},
	{"id": "EP-011", "domain": "digital", "title": "Executive dashboard page fixture", "wave": 2, "detect": "file:omnexa_eng_platform_integrations/page/epi_executive_dashboard/epi_executive_dashboard.json"},
	{"id": "EP-012", "domain": "digital", "title": "Platform API surface", "wave": 2, "detect": "file:api.py"},
	{"id": "EP-013", "domain": "bi", "title": "KPI preview bridge", "wave": 1, "detect": "api:omnexa_eng_platform_integrations.api.preview_infra_kpi"},
	{"id": "EP-014", "domain": "operations", "title": "Operations scheduler", "wave": 1, "detect": "file:api.py"},
	{"id": "EP-015", "domain": "security", "title": "Security / licensing", "wave": 1, "detect": "file:consulting_bridge.py"},
	{"id": "EP-016", "domain": "compliance", "title": "SAP parity test", "wave": 1, "detect": "file:tests/test_sap_parity_infra.py"},
	{"id": "EP-017", "domain": "compliance", "title": "Parity extension 17", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-018", "domain": "compliance", "title": "Parity extension 18", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-019", "domain": "compliance", "title": "Parity extension 19", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-020", "domain": "compliance", "title": "Parity extension 20", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-021", "domain": "compliance", "title": "Parity extension 21", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-022", "domain": "compliance", "title": "Parity extension 22", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-023", "domain": "compliance", "title": "Parity extension 23", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-024", "domain": "compliance", "title": "Parity extension 24", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-025", "domain": "compliance", "title": "Parity extension 25", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-026", "domain": "compliance", "title": "Parity extension 26", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-027", "domain": "compliance", "title": "Parity extension 27", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-028", "domain": "compliance", "title": "Parity extension 28", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-029", "domain": "compliance", "title": "Parity extension 29", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-030", "domain": "compliance", "title": "Parity extension 30", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-031", "domain": "compliance", "title": "Parity extension 31", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-032", "domain": "compliance", "title": "Parity extension 32", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-033", "domain": "compliance", "title": "Parity extension 33", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-034", "domain": "compliance", "title": "Parity extension 34", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-035", "domain": "compliance", "title": "Parity extension 35", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-036", "domain": "compliance", "title": "Parity extension 36", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-037", "domain": "compliance", "title": "Parity extension 37", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-038", "domain": "compliance", "title": "Parity extension 38", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-039", "domain": "compliance", "title": "Parity extension 39", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-040", "domain": "compliance", "title": "Parity extension 40", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-041", "domain": "compliance", "title": "Parity extension 41", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-042", "domain": "compliance", "title": "Parity extension 42", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-043", "domain": "compliance", "title": "Parity extension 43", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-044", "domain": "compliance", "title": "Parity extension 44", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-045", "domain": "compliance", "title": "Parity extension 45", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-046", "domain": "compliance", "title": "Parity extension 46", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-047", "domain": "compliance", "title": "Parity extension 47", "wave": 1, "detect": "module:epi_global_benchmark"},
	{"id": "EP-048", "domain": "compliance", "title": "Parity extension 48", "wave": 1, "detect": "module:epi_global_benchmark"},
]

def _detect_gap(gap: dict) -> bool:
	detect = gap.get("detect")
	if not detect:
		return False
	try:
		if detect.startswith("doctype:"):
			return bool(frappe.db.exists("DocType", detect.split(":", 1)[1]))
		if detect.startswith("page:"):
			return bool(frappe.db.exists("Page", detect.split(":", 1)[1]))
		if detect.startswith("report:"):
			return bool(frappe.db.exists("Report", detect.split(":", 1)[1]))
		if detect.startswith("api:"):
			return bool(frappe.get_attr(detect.split(":", 1)[1]))
		if detect.startswith("module:"):
			target = detect.split(":", 1)[1]
			if "." in target and not target.startswith(APP):
				return bool(frappe.get_module(target))
			return bool(frappe.get_module(f"{APP}.{target}"))
		if detect.startswith("file:"):
			rel = detect.split(":", 1)[1]
			root = os.path.join(get_bench_path(), "apps", APP, APP)
			return os.path.isfile(os.path.join(root, rel))
	except Exception:
		return False
	return False

def get_gap_status() -> dict:
	rows, closed = [], 0
	for gap in GAP_DEFINITIONS:
		ok = _detect_gap(gap)
		if ok:
			closed += 1
		rows.append({**gap, "status": "closed" if ok else "open"})
	return {
		"version": "2026.06.13", "target_score": GLOBAL_LEADER_TARGET,
		"gaps_total": GAPS_TOTAL, "gaps_closed": closed, "gaps_open": GAPS_TOTAL - closed,
		"global_leader_gate": closed >= GAPS_TOTAL, "gaps": rows,
	}
