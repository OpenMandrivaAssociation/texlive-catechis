Name:		texlive-catechis
Version:	59998
Release:	2
Summary:	Macros for typesetting catechisms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/catechis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros include: - format for question-and-answer; -
comments on answers; - citations; - a specialised enumerate
which only operates in the catechism parts of a document. The
macros are all highly customisable.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catechis
%doc %{_texmfdistdir}/doc/latex/catechis
#- source
%doc %{_texmfdistdir}/source/latex/catechis

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
