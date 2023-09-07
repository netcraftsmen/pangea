# pangea
Pangea has a comprehensive security platform that you can leverage with simple API calls for authentication, audit logging, secrets management, sensitive data removal, and intelligence services.

## Ansible Collection

This repository contains an Ansible Collection `collections/ansible_collections/netcraftsmen/pangea/` including a module `intel.py` to interface with Pangea Cloud. The collection `README.md` documents installation and use.

The `playbooks` directory contains two sample playbooks. Playbook `pb.intel_test.yml` is used to document the test cases. The playbook `pb.breach_user_check.yml` illustrates if a username, email or phone number has been exposed in a security breach. 

Refer to <https://galaxy.ansible.com/netcraftsmen/pangea>.

The motivation for developing this collection was to demonstrate a use case for the Pangea Securathon, but it has application for any Ansible automation where User, Domain or URL Intel adds value to the security posture of the infrastructure.

## Pangea Securathon

ABOUT THE CHALLENGE: Health & Wealth Hackathon is a great opportunity to build your security skills using Pangea APIs for more details see <https://healthandwealth.devpost.com/>. The deadline is 18 September 2023.

## Project Story

<!--- what inspired you, what you learned, how you built the project and the challenges you faced. --->

### Inspiration

The BlueAlly Consulting group has an active project to develop an automated workflow to manage the user database in Cisco Unified Communications Manager (CallManager) deployments. The project is based on developing an Ansible Content Collection for the client's Ansible Automation Platform to enable the workflow. By creating an Ansible Content Collection for Pangea User Intel, enables additional value to the client with a minimal development effort and cost.

### What it does

The BlueAlly Consulting group is engaged with a public university best known for its dental school, medical school, and college of engineering. As with any university, the students and faculty are transitory, having studied or taught at other colleges and as their tenure completes, enter the workforce. 

When onboarding students, employees, or faculty, an automated onboarding process should incorporate a breached user investigation, in addition to creating accounts for email and phone. Organizations frequently reallocate phone extensions and the username is often the same for both personal and corporate email accounts and passwords are frequently common between accounts as well.

As a value-add to customers, credit card companies offer identity monitoring services at low or no cost. Providing a similar service as part of the onboarding process is a valuable benefit and provides a proactive layer of protection from data breaches at work.

The Pangea User Intel service provides the ability to check a massive repository of breach data to identify if Personally Identifiable Information (PII) or credentials are exposed to criminal elements.

IBM's latest Cost of a Data Breach [reports](https://www.ibm.com/reports/data-breach) the average cost of a data breach is $4.45 million. The cost has increased by 2.3% and 15.3% respectively in the past two years. Breaches in the healthcare and financial sector are the highest cost across all industries.

BlueAlly Consulting can incorporate automation of breach detection, Using Red Hat Ansible Automation [Platform](https://www.redhat.com/en/technologies/management/ansible) and this Ansible Content Collection, during the onboarding process through the ITSM (IT Service Management) system. The results of the User Intel queries can be attached to the active ITSM ticket, a SOAR platform, or emailed allowing the Security Operations Center to identify and mitigate issues associated with past data breaches.

### How we built it

By creating a developer account on [pangea.cloud](https://console.pangea.cloud/) and exploring the tutorials and documentation on the Python [SDK](https://github.com/pangeacyber/pangea-python/tree/main/packages/pangea-sdk), a functional plugin/module was developed, tested, and documented in a few days of coding.

### Challenges we ran into

Really, no challenges at all. I am a big advocate of enabling a developer by way of community editions or developer accounts. This made the process very smooth and efficient. 

### Accomplishments that we're proud of

Enhancing the security posture of a client by offering an additional value-add at a reasonable cost.

### What we learned

The ability to query huge volumns of breach data with efficient API calls is amazing. 

### What's next for the project

We are excited to show this capability to our clients.

## Video demo link

A demo video of the project. <https://vimeo.com/manage/videos/859471646>

## Project Media

Refer to this repository or the DevPost site: <https://healthandwealth.devpost.com/>
<!--- jpg, png or gif format --->

## Author

Joel W. King (@joelwking)