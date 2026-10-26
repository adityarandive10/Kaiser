// Synthetic correction: role is assigned by trusted server-side logic.
function createStudentProfile(input) {
  return { name: input.name, role: "student" };
}
module.exports = { createStudentProfile };
