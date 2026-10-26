// Passing means the unsafe behavior was reproduced, not that security passed.
const assert = require("node:assert/strict");
const { createStudentProfile } = require("./status-vulnerable");
const profile = createStudentProfile({ name: "Demo", role: "admin" });
assert.equal(profile.role, "admin");
console.log("REPRODUCED: untrusted input can self-select the role");
