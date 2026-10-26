const assert = require("node:assert/strict");
const { createStudentProfile } = require("./status-fixed");
const profile = createStudentProfile({ name: "Demo", role: "admin" });
assert.equal(profile.role, "student");
assert.equal(profile.name, "Demo");
console.log("PASS: client-supplied role is ignored");
