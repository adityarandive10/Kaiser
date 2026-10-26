// Synthetic example only: role is taken from untrusted input.
function createStudentProfile(input) {
  return { name: input.name, role: input.role || "student" };
}
module.exports = { createStudentProfile };
